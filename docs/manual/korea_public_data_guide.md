# 🇰🇷 대한민국 공공데이터 활용 및 VoxCity 적용 가이드 (Korea Public Data Guide)

대한민국의 공공데이터 포털(국가공간정보포털, 국토정보플랫폼 등)에서 제공하는 고정밀 데이터를 활용하여 VoxCity에서 정교한 3D 도시 시뮬레이션을 수행하는 방법을 안내합니다.

글로벌 데이터 소스(OSM 등)보다 국내 실정에 맞는 정확한 건물 높이 및 지형 데이터를 사용할 수 있다는 장점이 있습니다.

---

## 1. 주요 데이터 수집 경로

### 🏢 건물 데이터 (Building Data)

| 데이터 명칭 | 수집처 | 주요 속성 | 특징 |
|:---|:---|:---|:---|
| **건물높이DB** | [국토정보플랫폼](https://map.ngii.go.kr) | `BLDH_BV` (실제 높이) | 가장 정확함 (미터 단위 실측값 포함) |
| **건물통합정보** | [국가공간정보포털](http://data.nsdi.go.kr) | `GRO_FLO_CO` (지상층수) | 층수 데이터를 통해 높이 추정 필요 |
| **연속수치지형도** | [국가공간정보포털] | 건물 레이어(A001) | 높이 값이 없는 경우 건축물대장과 결합 필요 |

> **추천**: `국토정보플랫폼`에서 제공하는 **[건물높이DB]**를 사용하는 것이 가장 정밀한 3D 모델을 생성할 수 있는 방법입니다.

### 🏔️ 지형 데이터 (DEM/Terrain)

- **수치지형도(DXF/SHP)**: 국토정보플랫폼에서 다운로드 가능. 등고선 데이터가 포함되어 있으나 VoxCity에서 직접 사용하려면 **GeoTIFF(DEM)** 형식으로 변환이 권장됩니다.
- **브이월드(V-World) API**: 3D 건물 서비스 API를 제공하지만, 원천 데이터(SHP) 추출은 제한적입니다. 배경지도로 활용하는 것이 좋습니다.

---

## 2. 데이터 전처리 (Pre-processing)

VoxCity에 적용하기 전, 다음 두 가지 사항을 반드시 확인해야 합니다.

### ⚠️ 좌표계 변환 (CRS Conversion)
국내 공공데이터는 주로 **EPSG:5179** (UTM-K) 또는 **EPSG:5186** (중부원점)을 사용합니다. VoxCity는 **EPSG:4326** (WGS84)을 기준으로 작동하므로 변환이 필수적입니다.

```python
import geopandas as gpd

# 데이터 로드
gdf = gpd.read_file("건물높이DB.shp")

# 좌표계 확인 및 변환 (EPSG:4326)
if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)
```

### 📏 높이 속성 정규화
VoxCity는 건물 폴리곤의 높이 속성명을 `'height'`로 인식합니다.

- **건물높이DB 사용 시**: `BLDH_BV` 컬럼을 `height`로 변경.
- **건물통합정보(층수) 사용 시**: 층당 약 3.0~3.5m로 계산하여 `height` 컬럼 생성.

```python
# 건물높이DB 사례
gdf = gdf.rename(columns={'BLDH_BV': 'height'})

# 층수 데이터 사례 (지상층수 GRO_FLO_CO 사용)
gdf['height'] = gdf['GRO_FLO_CO'] * 3.3
```

---

## 3. VoxCity 실제 적용 코드

가장 유연한 방법인 **GeoDataFrame 직접 전달** 방식을 권장합니다.

```python
import geopandas as gpd
from voxcity.generator import get_voxcity

# 1. 전처리된 공공데이터 준비
buildings = gpd.read_file("seoul_building_height_db.shp").to_crs(epsg=4326)
buildings = buildings.rename(columns={'BLDH_BV': 'height'})

# 2. 관심 영역 정의 (WGS84 좌표)
rectangle_vertices = [
    (126.973, 37.561), (126.973, 37.568),
    (126.982, 37.568), (126.982, 37.561)
]

# 3. VoxCity 모델 생성
# 건물은 로컬 공공데이터를 사용하고, 지형/토지피복은 자동 선택(OSM/GEE)하도록 설정
city = get_voxcity(
    rectangle_vertices,
    meshsize=2.0,  # 공공데이터 활용 시 고해상도(1~2m) 추천
    building_gdf=buildings,
    land_cover_source='OpenStreetMap', # 하이브리드 구성 가능
    **{"gridvis": True}
)

# 4. 결과 확인 및 내보내기
from voxcity.exporter.obj import export_obj
export_obj(city, "output", "seoul_public_data_model")
```

---

## 4. 고급 활용: 브이월드(V-World) 배경지도 시각화

시뮬레이션 결과를 브이월드 지도 위에 띄우고 싶은 경우, VoxCity의 시각화 도구와 브이월드 WMTS 서비스 연동을 고려할 수 있습니다.

### 💡 팁
- **수치지도 레이어 매핑**: 수치지형도의 `A001`(건물), `A002`(도로), `B001`(식생) 등을 각각 VoxCity의 건물, 도로 네트워크, 식생 데이터로 매핑하여 분석의 정확도를 높일 수 있습니다.
- **데이터 결합**: PNU(필지고유번호)를 기준으로 건축물대장(사용승인일, 구조 등)과 결합하면 **건물 노후도 분석**이나 **구조별 열환경 시뮬레이션**이 가능합니다.

---

이 가이드를 통해 대한민국의 정밀한 공공데이터를 VoxCity 프로젝트에 성공적으로 통합해 보시기 바랍니다.
