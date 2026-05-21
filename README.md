[![PyPi version](https://img.shields.io/pypi/v/voxcity.svg)](https://pypi.python.org/pypi/voxcity)
[![Python versions](https://img.shields.io/pypi/pyversions/voxcity.svg)](https://pypi.org/project/voxcity/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Lofd3RawKMr6QuUsamGaF48u2MN0hfrP?usp=sharing)
[![License](https://img.shields.io/pypi/l/voxcity.svg)](https://pypi.org/project/voxcity/)
[![Downloads](https://pepy.tech/badge/voxcity)](https://pepy.tech/project/voxcity)
[![Documentation Status](https://readthedocs.org/projects/voxcity/badge/?version=latest)](https://voxcity.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kunifujiwara/VoxCity/graph/badge.svg)](https://codecov.io/gh/kunifujiwara/VoxCity)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.compenvurbsys.2025.102366-blue)](https://doi.org/10.1016/j.compenvurbsys.2025.102366)

<p align="center">
  튜토리얼 미리보기: <a href="https://colab.research.google.com/drive/1Lofd3RawKMr6QuUsamGaF48u2MN0hfrP?usp=sharing">[Google Colab]</a> | 문서: <a href="https://voxcity.readthedocs.io/en/latest">[Read the Docs]</a> | 비디오 튜토리얼: <a href="https://youtu.be/qHusvKB07qk">[YouTube 시청]</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/logo.png" alt="Voxcity logo" width="550">
</p>

# VoxCity

**voxcity**는 전 세계 도시를 대상으로 그리드 기반의 3D 도시 모델 생성 및 도시 시뮬레이션을 위한 원스톱 솔루션을 제공하는 Python 패키지입니다. VoxCity의 생성기(generator) 모듈은 지정된 대상 영역 내의 건물 높이, 수관(canopy) 높이, 토지 피복(land cover) 및 지형 고도 데이터를 자동으로 다운로드하고, 이를 복셀화하여 건물, 나무, 토지 피복 및 지형이 통합된 복셀 도시 모델을 생성합니다. 시뮬레이터(simulator) 모듈을 사용하면 태양 복사(solar radiation) 및 가시 지수(view index) 분석과 같은 환경 시뮬레이션을 수행할 수 있습니다. 생성된 모델은 ENVI-met (INX), Blender, Rhino (OBJ) 등 외부 소프트웨어와 호환되는 여러 파일 형식으로 내보낼 수 있습니다. [Google Colab 데모](https://colab.research.google.com/drive/1Lofd3RawKMr6QuUsamGaF48u2MN0hfrP?usp=sharing) 또는 로컬 환경에서 직접 사용해 보세요. 자세한 문서, API 레퍼런스 및 튜토리얼은 [Read the Docs](https://voxcity.readthedocs.io/en/latest) 페이지를 방문해 확인하실 수 있습니다.

<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/concept.png" alt="Conceptual Diagram of voxcity" width="800">
</p>

## 튜토리얼 (Tutorial)

### Google Colab 데모

| 데모 | 설명 | 링크 |
|------|-------------|------|
| **기본 가이드** | 복셀 도시 모델 생성, 시각화 및 내보내기 | <a href="https://colab.research.google.com/drive/1Lofd3RawKMr6QuUsamGaF48u2MN0hfrP?usp=sharing">Colab에서 열기</a> |
| **ENVI-met 내보내기** | VoxCity 모델을 ENVI-met INX 형식으로 내보내기 | <a href="https://colab.research.google.com/drive/1Yv7hMmfEiygCbuz5gPfGmCZyVQnr-8Qn">Colab에서 열기</a> |

### YouTube 비디오

- **둘러보기(Walkthrough)**: <a href="https://youtu.be/qHusvKB07qk">YouTube에서 시청하기</a>

<p align="center">
  <a href="https://youtu.be/qHusvKB07qk" title="YouTube에서 VoxCity 튜토리얼 시청하기">
    <img src="images/youtube_thumbnail_play.png" alt="VoxCity 튜토리얼 — YouTube 시청을 위해 클릭하세요" width="480">
  </a>
</p>

<p align="center">
  <em>튜토리얼 비디오 제작: <a href="https://ual.sg/author/xiucheng-liang/">Xiucheng Liang</a></em>
</p>

## 주요 기능 (Key Features)

- **다양한 데이터 소스 통합:**  
  건물 풋프린트, 토지 피복 데이터, 수관 높이 맵, DEM을 결합하여 도시 경관의 일관된 3D 복셀 표현을 생성합니다.
  
- **유연한 입력 소스:**  
  다음을 포함한 다양한 건물 및 지형 데이터 소스를 지원합니다:
  - 건물 풋프린트: OpenStreetMap, Overture, EUBUCCO, Microsoft Building Footprints, Open Building 2.5D
  - 토지 피복: UrbanWatch, OpenEarthMap Japan, ESA WorldCover, ESRI Land Cover, Dynamic World, OpenStreetMap
  - 수관 높이: 고해상도 1m 글로벌 수관 높이 맵, ETH Global Sentinel-2 10m
  - DEM: DeltaDTM, FABDEM, NASA, COPERNICUS 등

  *각 데이터 소스에 대한 자세한 정보는 [데이터 소스 참고 문헌](#references-of-data-sources) 섹션에서 확인할 수 있습니다.*
  
- **사용자 정의 가능한 도메인 및 해상도:**  
  지도에 사각형을 그리거나 중심 좌표와 크기를 지정하여 대상 영역을 쉽게 정의할 수 있습니다. 필요에 따라 메쉬 크기(해상도)를 조정하세요.
  
- **Earth Engine 통합:**  
  대규모 지형 공간 데이터 처리를 위해 Google Earth Engine을 활용합니다 (인증 및 프로젝트 설정 필요).
  
- **출력 형식:**
  - **ENVI-MET**: 미세 기후 시뮬레이션에 적합한 INX 및 EDB 파일 내보내기.
  - **MagicaVoxel**: MagicaVoxel에서 3D 편집 및 시각화를 위한 vox 파일 내보내기.
  - **OBJ**: 렌더링 및 다른 워크플로우 통합을 위한 Wavefront OBJ 내보내기.

- **분석 도구:**
  - **가시 지수 시뮬레이션**: 지정된 시점에서의 천공율(SVI) 및 녹시율(GVI) 계산.
  - **랜드마크 가시성 맵**: 복셀화된 환경 내에서 선택된 랜드마크의 가시성 평가.

## 설치 방법 (Installation)

Python 3.12가 설치되어 있어야 합니다. 다음 명령어로 voxcity를 설치할 수 있습니다:

### 로컬 환경의 경우

```bash
conda create --name voxcity python=3.12
conda activate voxcity
conda install -c conda-forge gdal timezonefinder
pip install voxcity
```

### Google Colab의 경우

```python
!pip install voxcity
```

## Earth Engine 설정

Earth Engine 데이터를 사용하려면 다음 지침에 따라 Earth Engine이 활성화된 Cloud 프로젝트를 설정하세요:
https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup

설정 후, Earth Engine을 인증하고 초기화합니다:

### 로컬 환경의 경우

```bash
earthengine authenticate
```

### Google Colab의 경우

```python
# 표시된 링크를 클릭하고 토큰을 생성한 뒤, 토큰을 복사하여 붙여넣으세요.
!earthengine authenticate --auth_mode=notebook
```

## 사용법 개요 (Usage Overview)

### 1. Earth Engine 인증

```python
import ee
ee.Authenticate()
ee.Initialize(project='your-project-id')
```

### 2. 대상 구역 정의

세 가지 방법으로 대상 구역을 정의할 수 있습니다:

#### 옵션 1: 직접 좌표 입력
사각형 꼭짓점의 좌표를 직접 지정하여 대상 구역을 정의합니다.

```python
rectangle_vertices = [
    (-122.33587348582083, 47.59830044521263),  # 남서쪽 모서리 (경도, 위도)
    (-122.33587348582083, 47.60279755390168),  # 북서쪽 모서리 (경도, 위도) 
    (-122.32922451417917, 47.60279755390168),  # 북동쪽 모서리 (경도, 위도)
    (-122.32922451417917, 47.59830044521263)   # 남동쪽 모서리 (경도, 위도)
]
```

#### 옵션 2: 사각형 그리기 (Jupyter Notebook용)
GUI 지도 인터페이스를 사용하여 관심 있는 사각형 영역을 그립니다.

```python
from voxcity.geoprocessor.draw import draw_rectangle_map_cityname

cityname = "tokyo"
m, rectangle_vertices = draw_rectangle_map_cityname(cityname, zoom=15)
m
```

#### 옵션 3: 중심 및 크기 지정 (Jupyter Notebook용)
미터 단위의 너비와 높이를 선택하고 지도에서 중심점을 선택합니다.

```python
from voxcity.geoprocessor.draw import center_location_map_cityname

width = 500
height = 500
m, rectangle_vertices = center_location_map_cityname(cityname, width, height, zoom=15)
m
```
<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/draw_rect.png" alt="Draw Rectangle on Map GUI" width="400">
</p>

### 3. 매개변수 설정

메쉬 크기(필수)와 선택적 데이터 소스를 정의합니다:

```python
meshsize = 5  # 미터 단위의 그리드 셀 크기 (필수)

# 선택 사항: 출력 디렉토리 및 기타 설정 지정
kwargs = {
    "output_dir": "output",   # 출력 파일 저장 디렉토리
    "dem_interpolation": True # DEM 보간 활성화
}
```

### 4. voxcity 출력 획득

복셀 데이터 그리드와 해당 건물의 GeoDataFrame을 생성합니다.

#### 옵션 1: 자동 모드 (권장)
위치에 따라 데이터 소스가 자동으로 선택됩니다:

```python
from voxcity.generator import get_voxcity

# 자동 모드: 위치를 기반으로 모든 데이터 소스가 자동으로 선택됨
voxcity = get_voxcity(
    rectangle_vertices,
    meshsize,
    **kwargs
)
```

#### 옵션 2: 사용자 정의 모드
데이터 소스를 명시적으로 지정합니다:

```python
# 사용자 정의 모드: 모든 데이터 소스를 명시적으로 지정
voxcity = get_voxcity(
    rectangle_vertices,
    meshsize,
    building_source='OpenStreetMap',
    land_cover_source='OpenStreetMap',
    canopy_height_source='High Resolution 1m Global Canopy Height Maps',
    dem_source='DeltaDTM',
    **kwargs
)
```

#### 옵션 3: 하이브리드 모드
일부 소스는 지정하고 나머지는 자동 선택합니다:

```python
# 하이브리드 모드: 건물 소스는 지정하고 나머지는 자동 선택
voxcity = get_voxcity(
    rectangle_vertices,
    meshsize,
    building_source='Overture',  # 사용자 지정
    # land_cover_source, canopy_height_source, dem_source는 자동 선택됨
    **kwargs
)
```

### 대화형 3D 데모 (Plotly)

- **대화형 데모 열기**: <a href="https://voxcity.readthedocs.io/en/latest/_static/plotly/voxcity_demo.html">Plotly 3D 뷰어 실행</a>

### 5. 파일 내보내기 (Exporting Files)

#### ENVI-MET INX/EDB 파일:
[ENVI-MET](https://www.envi-met.com/)은 도시 환경 모델링에 특화된 고급 미세 기후 시뮬레이션 소프트웨어입니다. 건물, 식생, 그리고 온도, 풍향, 습도, 복사와 같은 다양한 기후 매개변수 간의 상호작용을 시뮬레이션합니다. 이 소프트웨어는 도시 계획, 건축 및 환경 연구에서 널리 사용됩니다 (상업용, 교육용 라이선스 제공).

```python
from voxcity.exporter.envimet import export_inx, generate_edb_file

envimet_kwargs = {
    "output_directory": "output",            # 출력 파일 저장 디렉토리
    "file_basename": "voxcity",              # INX용 기본 이름 (확장자 제외)
    "author_name": "your name",              # 모델 제작자 이름
    "model_description": "generated with voxcity",  # 모델 설명
    "domain_building_max_height_ratio": 2,   # 도메인 높이와 가장 높은 건물 간의 최대 비율
    "useTelescoping_grid": True,             # 텔레스코핑 그리드 활성화
    "verticalStretch": 20,                   # 수직 그리드 신축 계수 (%)
    "min_grids_Z": 20,                       # 최소 수직 그리드 셀 수
    "lad": 1.0                               # EDB 생성을 위한 엽면적 밀도 (LAD, m2/m3)
}

# 선택 사항: 내보내기에 사용할 토지 피복 소스 지정 (지정하지 않으면 가능한 경우 voxcity.extras에서 가져옴)
land_cover_source = 'OpenStreetMap'

# VoxCity 객체를 직접 전달하여 INX 내보내기
export_inx(
    voxcity,
    output_directory=envimet_kwargs["output_directory"],
    file_basename=envimet_kwargs["file_basename"],
    land_cover_source=land_cover_source,
    author_name=envimet_kwargs["author_name"],
    model_description=envimet_kwargs["model_description"],
    domain_building_max_height_ratio=envimet_kwargs["domain_building_max_height_ratio"],
    useTelescoping_grid=envimet_kwargs["useTelescoping_grid"],
    verticalStretch=envimet_kwargs["verticalStretch"],
    min_grids_Z=envimet_kwargs["min_grids_Z"],
)

# 식생을 위한 식물 데이터베이스(EDB) 생성
generate_edb_file(lad=envimet_kwargs["lad"])
```
<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/envimet.png" alt="Generated 3D City Model on Envi-MET GUI" width="600">
</p>
<p align="center">
  <em>INX로 내보낸 후 ENVI-met에서 불러온 출력 예시</em>
</p>

#### OBJ 파일:

```python
from voxcity.exporter.obj import export_obj

output_directory = "output"  # 출력 파일 저장 디렉토리
output_file_name = "voxcity" # 출력 OBJ 파일의 기본 이름
# VoxCity 객체를 직접 전달 (복셀 크기 유추됨)
export_obj(voxcity, output_directory, output_file_name)
```
생성된 OBJ 파일은 다음 3D 시각화 소프트웨어에서 열고 렌더링할 수 있습니다:

- [Twinmotion](https://www.twinmotion.com/): 실시간 시각화 도구 (개인용 무료)
- [Blender](https://www.blender.org/): 전문가급 3D 제작 제품군 (무료)
- [Rhino](https://www.rhino3d.com/): 전문 3D 모델링 소프트웨어 (상업용, 교육용 라이선스 제공)

<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/obj.png" alt="OBJ 3D City Model Rendered in Rhino" width="600">
</p>
<p align="center">
  <em>OBJ로 내보낸 후 Rhino에서 렌더링한 출력 예시</em>
</p>

#### MagicaVoxel VOX 파일:

[MagicaVoxel](https://ephtracy.github.io/)은 가볍고 사용자 친화적인 복셀 아트 편집기입니다. 직관적인 인터페이스로 복셀 기반 3D 모델을 생성, 편집 및 렌더링할 수 있어 복셀화된 도시 모델을 수정하고 시각화하는 데 적합합니다. 이 소프트웨어는 무료이며 Windows 및 Mac에서 사용할 수 있습니다.

```python
from voxcity.exporter.magicavoxel import export_magicavoxel_vox

output_path = "output"
base_filename = "voxcity"
# VoxCity 객체 직접 전달
export_magicavoxel_vox(voxcity, output_path, base_filename=base_filename)
```
<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/vox.png" alt="Generated 3D City Model on MagicaVoxel GUI" width="600">
</p>
<p align="center">
  <em>VOX로 내보낸 후 MagicaVoxel에서 렌더링한 출력 예시</em>
</p>

### 6. 추가 활용 사례

#### 일사량(Solar Irradiance) 계산:

```python
from voxcity.simulator.solar import get_global_solar_irradiance_using_epw

solar_kwargs = {
    "download_nearest_epw": True,  # Climate.OneBuilding.Org에서 위치 기반으로 가장 가까운 EPW 기상 파일을 자동으로 다운로드할지 여부
    # "epw_file_path": "./output/new.york-downtown.manhattan.heli_ny_usa_1.epw",  # 기상 데이터를 포함하는 EnergyPlus Weather(EPW) 파일 경로. 이미 파일이 있는 경우 설정하세요.
    "calc_time": "01-01 12:00:00",  # "MM-DD HH:MM:SS" 형식의 순간 계산 시간
    "view_point_height": 1.5,  # 일사 접근성을 계산할 시점의 높이(미터). 기본값: 1.5 m
    "tree_k": 0.6,    # 정적 소멸 계수 - 나무에 의해 햇빛이 차단되는 양을 조절 (높을수록 더 많이 차단)
    "tree_lad": 1.0,    # 나무의 엽면적 밀도 - 그림자에 영향을 미치는 잎/가지의 밀도 (높을수록 무성한 잎)
    "colormap": 'magma',       # 시각화를 위한 Matplotlib 컬러맵. 기본값: 'viridis'
    "obj_export": True,        # 결과를 3D OBJ 파일로 내보낼지 여부
    "output_directory": 'output/test',  # 출력 파일 저장 디렉토리
    "output_file_name": 'instantaneous_solar_irradiance',  # 출력 기본 파일 이름 (확장자 제외)
    "alpha": 1.0,             # 시각화 투명도 (0.0-1.0)
    "vmin": 0,               # 시각화에서 컬러맵 배율의 최소값
    # "vmax": 900,             # 시각화에서 컬러맵 배율의 최대값
}

# 전체 일사량 맵 계산 (직달 + 확산 복사)
solar_grid = get_global_solar_irradiance_using_epw(
    voxcity,                             # 복셀 데이터 및 메타데이터를 포함하는 VoxCity 객체
    calc_type='instantaneous',           # 지정된 시점의 순간 일사량 계산
    direct_normal_irradiance_scaling=1.0, # 직달 일사량 보정 계수 (1.0 = 보정 없음)
    diffuse_irradiance_scaling=1.0,      # 확산 일사량 보정 계수 (1.0 = 보정 없음)
    **solar_kwargs                       # 위에서 정의한 모든 매개변수 전달
)

# 누적 계산을 위한 매개변수 조정
solar_kwargs["start_time"] = "01-01 01:00:00" # 누적 계산 시작 시간
solar_kwargs["end_time"] = "01-31 23:00:00" # 누적 계산 종료 시간
solar_kwargs["output_file_name"] = 'cumulative_solar_irradiance'  # 출력 기본 파일 이름 (확장자 제외)

# 지정된 기간 동안의 누적 일사량 계산
cum_solar_grid = get_global_solar_irradiance_using_epw(
    voxcity,                             # 복셀 데이터 및 메타데이터를 포함하는 VoxCity 객체
    calc_type='cumulative',              # 순간값이 아닌 기간 동안의 누적 일사량 계산
    direct_normal_irradiance_scaling=1.0, # 직달 일사량 보정 계수 (1.0 = 보정 없음)
    diffuse_irradiance_scaling=1.0,      # 확산 일사량 보정 계수 (1.0 = 보정 없음)
    **solar_kwargs                       # 위에서 정의한 모든 매개변수 전달
)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/solar.png" alt="Solar Irradiance Maps Rendered in Rhino" width="800">
</p>
<p align="center">
  <em>OBJ로 저장한 후 Rhino에서 렌더링한 결과 예시</em>
</p>

#### 녹시율(GVI) 및 천공율(SVI) 계산:

```python
from voxcity.simulator.view import get_view_index

view_kwargs = {
    "view_point_height": 1.5,      # 관찰자 시점 높이 (미터 단위)
    "colormap": "viridis",         # 시각화용 컬러맵
    "obj_export": True,            # OBJ 파일 내보내기 여부
    "output_directory": "output",  # 출력 파일 저장 디렉토리
    "output_file_name": "gvi"      # 출력 기본 파일 이름
}

# mode='green'을 사용하여 녹시율(GVI) 계산
gvi_grid = get_view_index(voxcity, mode='green', **view_kwargs)

# 천공율(SVI)을 위한 매개변수 조정
view_kwargs["colormap"] = "BuPu_r"
view_kwargs["output_file_name"] = "svi"
view_kwargs["elevation_min_degrees"] = 0 # 지평선부터 레이 트레이싱 시작

# mode='sky'를 사용하여 천공율(SVI) 계산
svi_grid = get_view_index(voxcity, mode='sky', **view_kwargs)
```
<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/view_index.png" alt="View Index Maps Rendered in Rhino" width="800">
</p>
<p align="center">
  <em>OBJ로 저장한 후 Rhino에서 렌더링한 결과 예시</em>
</p>

#### 랜드마크 가시성 맵:

```python
from voxcity.simulator.view import get_landmark_visibility_map

# 랜드마크 가시성 분석 매개변수 딕셔너리
landmark_kwargs = {
    "view_point_height": 1.5,                 # 관찰자 시점 높이 (미터 단위)
    "colormap": "cool",                       # 시각화용 컬러맵
    "obj_export": True,                       # OBJ 파일 내보내기 여부
    "output_directory": "output",             # 출력 파일 저장 디렉토리
    "output_file_name": "landmark_visibility" # 출력 기본 파일 이름
}
landmark_vis_map, _ = get_landmark_visibility_map(voxcity, voxcity.extras.get('building_gdf'), **landmark_kwargs)
```
<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/landmark.png" alt="Landmark Visibility Map Rendered in Rhino" width="500">
</p>
<p align="center">
  <em>OBJ로 저장한 후 Rhino에서 렌더링한 결과 예시</em>
</p>

#### 네트워크 분석:

```python
from voxcity.geoprocessor.network import get_network_values

network_kwargs = {
    "network_type": "walk",        # OSM에서 다운로드할 네트워크 유형 (walk, drive, all 등)
    "colormap": "magma",          # 시각화용 Matplotlib 컬러맵
    "vis_graph": True,            # 네트워크 시각화 표시 여부
    "vmin": 0.0,                  # 색상 배율의 최소값
    "vmax": 600000,               # 색상 배율의 최대값
    "edge_width": 2,              # 시각화 시 네트워크 에지 너비
    "alpha": 0.8,                 # 네트워크 에지의 투명도
    "zoom": 16                    # 배경 지도의 줌 레벨
}

G, edge_gdf = get_network_values(
    cum_solar_grid,               # 누적 일사량 값의 그리드
    rectangle_vertices,           # 시뮬레이션 도메인 경계를 정의하는 좌표
    meshsize,                     # 각 그리드 셀의 크기 (미터 단위)
    value_name='Cumulative Global Solar Irradiance (W/m²·hour)',  # 시각화에서의 값 레이블
    **network_kwargs              # 추가적인 시각화 및 네트워크 매개변수
)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/kunifujiwara/VoxCity/main/images/network.png" alt="Example of Graph Output" width="500">
</p>
<p align="center">
  <em>도로 네트워크상에서의 연간 누적 전체 일사량 (kW/m²·hour)</em>
</p>

## VoxCity 표준 토지 피복 클래스 (복셀 그리드에 사용됨)

| 인덱스 | 클래스 | 인덱스 | 클래스 |
|:-----:|-------|:-----:|-------|
| 1 | 나대지 (Bareland) | 8 | 망그로브 (Mangrove) |
| 2 | 목초지 (Rangeland) | 9 | 수역 (Water) |
| 3 | 관목 (Shrub) | 10 | 눈과 얼음 (Snow and ice) |
| 4 | 농경지 (Agriculture land) | 11 | 개발지 (Developed space) |
| 5 | 나무 (Tree) | 12 | 도로 (Road) |
| 6 | 지의류 및 이끼 (Moss and lichen) | 13 | 건물 (Building) |
| 7 | 습지 (Wet land) | 14 | 데이터 없음 (No Data) |

## 데이터 소스 참고 문헌 (References of Data Sources)

### 건물 (Building)

| 데이터셋 | 공간 범위 | 출처 / 데이터 획득 |
|---------|------------------|------------------------|
| [OpenStreetMap](https://www.openstreetmap.org) | 전 세계 (도심지 약 24% 완성도) | 자원봉사자 참여 / 지속적 업데이트 |
| [Microsoft Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) | 북미, 유럽, 호주 | 위성 또는 항공 영상 기반 예측 / 대다수 영상이 2018-2019년 기준 |
| [Open Buildings 2.5D Temporal Dataset](https://sites.research.google/gr/open-buildings/temporal/) | 아프리카, 라틴 아메리카, 남부 및 동남아시아 | 위성 영상 기반 예측 / 2016-2023 |
| [EUBUCCO v0.1](https://eubucco.com/) | EU 27개국 및 스위스 (378개 지역, 40,829개 도시) | OSM, 정부 데이터셋 / 2003-2021 (대부분 2019년 이후) |
| [UT-GLOBUS](https://zenodo.org/records/11156602) | 전 세계 (1,200개 이상의 도시 및 지역) | 건물 풋프린트, 인구, 위성 nDSM 기반 예측 / 미제공 |
| [Overture Maps](https://overturemaps.org/) | 전 세계 | OSM, Esri Community Maps, Google Open Buildings 등 / 지속적 업데이트 |

### 수관 높이 (Tree Canopy Height)

| 데이터셋 | 범위 | 해상도 | 출처 / 데이터 획득 |
|---------|-----------|------------|------------------------|
| [High Resolution 1m Global Canopy Height Maps](https://sustainability.atmeta.com/blog/2024/04/22/using-artificial-intelligence-to-map-the-earths-forests/) | 전 세계 | 1 m | 위성 영상 기반 예측 / 2009 및 2020 (80%가 2018-2020년) |
| [ETH Global Sentinel-2 10m Canopy Height (2020)](https://langnico.github.io/globalcanopyheight/) | 전 세계 | 10 m | 위성 영상 기반 예측 / 2020 |

### 토지 피복 (Land Cover)

| 데이터셋 | 공간 범위 | 해상도 | 출처 / 데이터 획득 |
|---------|------------------|------------|----------------------|
| [ESA World Cover 10m 2021 V200](https://zenodo.org/records/7254221) | 전 세계 | 10 m | 위성 영상 기반 예측 / 2021 |
| [ESRI 10m Annual Land Cover (2017-2023)](https://www.arcgis.com/home/item.html?id=cfcb7609de5f478eb7666240902d4d3d) | 전 세계 | 10 m | 위성 영상 기반 예측 / 2017-2023 |
| [Dynamic World V1](https://dynamicworld.app) | 전 세계 | 10 m | 위성 영상 기반 예측 / 지속적 업데이트 |
| [OpenStreetMap](https://www.openstreetmap.org) | 전 세계 | - (벡터) | 자원봉사자 참여 / 지속적 업데이트 |
| [OpenEarthMap Japan](https://www.open-earth-map.org/demo/Japan/leaflet.html) | 일본 | ~1 m | 항공 영상 기반 예측 / 1974-2022 (주요 도시는 대부분 2018년 이후) |
| [UrbanWatch](https://urbanwatch.charlotte.edu/) | 미국 22개 주요 도시 | 1 m | 항공 영상 기반 예측 / 2014–2017 |

### 지형 고도 (Terrain Elevation)

| 데이터셋 | 범위 | 해상도 | 출처 / 데이터 획득 |
|---------|-----------|------------|------------------------|
| [FABDEM](https://doi.org/10.5523/bris.25wfy0f9ukoge2gs7a5mqpq2j7) | 전 세계 | 30 m | 수관 높이 및 건물 풋프린트를 사용한 Copernicus DEM 보정 / 2011-2015 (Copernicus DEM) |
| [DeltaDTM](https://gee-community-catalog.org/projects/delta_dtm/) | 전 세계 (고도 10m 이하 해안 지역 + 평균 해수면) | 30 m | Copernicus DEM, 위성 LiDAR / 2011-2015 (Copernicus DEM) |
| [USGS 3DEP 1m DEM](https://www.usgs.gov/3d-elevation-program) | 미국 | 1 m | 항공 LiDAR / 2004-2024 (대부분 2015년 이후) |
| [England 1m Composite DTM](https://environment.data.gov.uk/dataset/13787b9a-26a4-4775-8523-806d13af58fc) | 영국 잉글랜드 | 1 m | 항공 LiDAR / 2000-2022 |
| [Australian 5M DEM](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/89644) | 호주 | 5 m | 항공 LiDAR / 2001-2015 |
| [RGE Alti](https://geoservices.ign.fr/rgealti) | 프랑스 | 1 m | 항공 LiDAR |

## 인용 (Citation)

학술 간행물에서 `voxcity`를 사용하는 경우 다음 [논문](https://doi.org/10.1016/j.compenvurbsys.2025.102366)을 인용해 주세요:

Fujiwara K, Tsurumi R, Kiyono T, Fan Z, Liang X, Lei B, Yap W, Ito K, Biljecki F., 2026. VoxCity: A Seamless Framework for Open Geospatial Data Integration, Grid-Based Semantic 3D City Model Generation, and Urban Environment Simulation. Computers, Environment and Urban Systems, 123, p.102366. https://doi.org/10.1016/j.compenvurbsys.2025.102366

```bibtex
@article{fujiwara2025voxcity,
  title={VoxCity: A Seamless Framework for Open Geospatial Data Integration, Grid-Based Semantic 3D City Model Generation, and Urban Environment Simulation},
  author={Fujiwara, Kunihiko and Tsurumi, Ryuta and Kiyono, Tomoki and Fan, Zicheng and Liang, Xiucheng and Lei, Binyu and Yap, Winston and Ito, Koichi and Biljecki, Filip},
  journal={Computers, Environment and Urban Systems},
  volume = {123},
  pages = {102366},
  year = {2026},
  doi = {10.1016/j.compenvurbsys.2025.102366}
}
```

## 공로 (Credit)

 - 튜토리얼 비디오 제작: <a href="https://ual.sg/author/xiucheng-liang/">Xiucheng Liang</a>

이 패키지는 [Cookiecutter](https://github.com/audreyr/cookiecutter)와 [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) 프로젝트 템플릿으로 생성되었습니다.

--------------------------------------------------------------------------------
<br>
<br>
<p align="center">
  <a href="https://ual.sg/">
    <img src="https://raw.githubusercontent.com/winstonyym/urbanity/main/images/ualsg.jpeg" width = 55% alt="Logo">
  </a>
</p>
