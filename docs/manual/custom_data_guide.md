# 📂 사용자 정의 데이터 및 공공데이터 활용 가이드 (Custom & Public Data Guide)

VoxCity는 기본적으로 제공되는 글로벌 데이터 소스(OpenStreetMap, Google Open Buildings 등) 외에도, 사용자가 직접 제작한 데이터나 공공데이터 포털에서 내려받은 지형 공간 데이터를 활용하여 3D 복셀 모델을 생성하고 분석할 수 있는 강력한 기능을 제공합니다.

이 가이드는 외부 데이터를 VoxCity 파이프라인에 통합하는 방법과 시각화 및 주요 주의 사항을 다룹니다.

---

## 1. 데이터 카테고리별 요구 사항

VoxCity에서 사용하는 데이터는 크게 **벡터(Vector)**와 **래스터(Raster)** 형식으로 나뉩니다.

### 🏢 건물 데이터 (Building Data)
- **형식**: GeoPackage (.gpkg), GeoJSON (.json/.geojson), Shapefile (.shp) 등
- **필수 속성**: 기하구조(Polygon/MultiPolygon)
- **권장 속성**: `height` (건물 높이, 미터 단위). 속성이 없으면 기본값(기본 10m)이 적용됩니다.

### 🏔️ 지형 데이터 (DEM/Terrain)
- **형식**: GeoTIFF (.tif) - 권장, 또는 벡터 형식
- **필수 데이터**: 고도 값(Elevation). 벡터 형식의 경우 `elevation` 컬럼이 필요합니다.

### 🌳 식생 데이터 (Canopy/Vegetation)
- **형식**: GeoPackage (.gpkg) 또는 GeoPandas GeoDataFrame
- **필수 속성**: `height` (나무의 최대 높이, 미터 단위)

### 🌍 토지 피복 데이터 (Land Cover)
- **형식**: GeoTIFF (.tif)
- **주의**: 고유한 색상(RGB) 또는 인덱스 값이 VoxCity 표준 클래스로 매핑되어야 합니다.

---

## 2. 로컬 파일을 이용한 데이터 로드 방법

`get_voxcity()` 함수를 호출할 때 데이터 소스를 `'Local file'`로 지정하고 파일 경로를 전달합니다.

```python
from voxcity.generator import get_voxcity

# 관심 지역 정의 (예시: 서울)
rectangle_vertices = [
    (126.97, 37.56), (126.97, 37.57), 
    (126.98, 37.57), (126.98, 37.56)
]

kwargs = {
    # 건물 데이터 설정
    "building_path": "path/to/your/buildings.gpkg",
    
    # 지형 데이터(DEM) 설정
    "dem_path": "path/to/your/dem.tif",
    
    # 출력 설정
    "output_dir": "output/custom_project",
    "gridvis": True
}

city = get_voxcity(
    rectangle_vertices,
    meshsize=5,
    building_source='Local file',
    dem_source='Local file',
    **kwargs
)
```

---

## 3. GeoPandas 객체(GeoDataFrame) 직접 전달 (고급)

파일 경로 대신 이미 메모리에 로드된 `GeoDataFrame`을 직접 전달할 수 있습니다. 이 방법은 데이터를 전처리(필터링, 좌표계 변환 등)한 후 즉시 사용하고 싶을 때 매우 유용합니다.

```python
import geopandas as gpd
from voxcity.generator import get_voxcity

# 공공데이터 로드 및 전처리
my_buildings = gpd.read_file("seoul_buildings.shp")
# 반드시 EPSG:4326(WGS84)으로 변환할 필요는 없으나 권장됨 (내부적으로 자동 변환 시도)
my_buildings = my_buildings.to_crs(epsg=4326)

# 속성명 매핑 (필요시)
my_buildings = my_buildings.rename(columns={'BLD_HGT': 'height'})

city = get_voxcity(
    rectangle_vertices,
    meshsize=2,
    building_gdf=my_buildings,  # GDF 직접 전달
    # 다른 소스는 자동 선택하거나 Local file 사용 가능
    **kwargs
)
```

---

## 4. 공공데이터 활용 팁 (대한민국 사례)

대한민국 내 프로젝트를 진행할 때 유용한 공공데이터 소스와 처리 방법입니다.

### 📍 주요 데이터 소스
1.  **국가공간정보포털 (NSDI)**: 연속수치지형도(건물, 도로 등)를 SHP 형식으로 제공합니다.
2.  **서울 열린데이터 광장**: 서울시 건축물 고도 및 풋프린트 데이터를 제공합니다.
3.  **V-World**: API를 통해 건물 및 지형 데이터를 획득할 수 있습니다.

### ⚠️ 좌표계 변환 (CRS)
국내 공공데이터는 주로 **EPSG:5179** (UTM-K)나 **EPSG:5186** (중부원점) 등을 사용합니다. VoxCity는 글로벌 표준인 **EPSG:4326** (WGS84)를 기반으로 작동하므로, 데이터를 로드한 후 변환해 주는 것이 안전합니다.

```python
gdf = gpd.read_file("data.shp").to_crs(epsg=4326)
```

---

## 5. 시각화 방법 (Visualization)

데이터를 로드한 후, 다양한 방법으로 시각화하여 검증할 수 있습니다.

### 2D 그리드 시각화
`get_voxcity` 호출 시 `gridvis=True`를 설정하면, 각 데이터 그리드(건물 높이, DEM 등)가 정적 이미지로 출력됩니다.

### 3D 대화형 시각화 (Plotly)
노트북 환경에서 3D 모델을 회전하고 확대하며 확인할 수 있습니다.
```python
from voxcity.visualizer.renderer import visualize_voxcity_plotly

visualize_voxcity_plotly(
    city.voxels.classes,
    city.voxels.meta.meshsize,
    title="Custom Data 3D Model"
)
```

### 시뮬레이션 결과 중첩 시각화
자체 시뮬레이션 결과(2D 그리드)를 3D 모델 위에 겹쳐서 시각화할 수 있습니다.
```python
# 예: custom_result_grid가 (nx, ny) 형태의 넘파이 배열인 경우
visualize_voxcity_plotly(
    city.voxels.classes,
    city.voxels.meta.meshsize,
    ground_sim_grid=custom_result_grid,
    ground_colormap='hot',
    title="Custom Simulation Result"
)
```

### 3D 모델 및 분석 결과 내보내기 (OBJ)
외부 도구(Blender, Rhino)에서 정밀하게 시각화하거나 렌더링하고 싶을 때 사용합니다.
```python
from voxcity.exporter.obj import export_obj, grid_to_obj

# 1. 전체 복셀 모델 내보내기
export_obj(city, "output", "custom_model")

# 2. 특정 분석 결과만 색상화된 지표면으로 내보내기
grid_to_obj(
    custom_result_grid,
    output_dir="output",
    file_name="simulation_result",
    cell_size=5,
    colormap_name='viridis'
)
```

---

VoxCity는 다양한 소스의 결합을 지원하므로, 예를 들어 **지형은 고해상도 로컬 데이터**를 사용하고 **건물은 OpenStreetMap**에서 가져오는 식의 하이브리드 구성도 가능합니다.
