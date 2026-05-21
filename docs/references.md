# 참고 문헌 (References)

VoxCity는 그리드 기반의 3D 도시 모델 생성 및 도시 시뮬레이션을 위한 종합적인 Python 패키지입니다. 아래의 참고 문헌들은 VoxCity에서 사용된 도구와 데이터셋의 원저작자들에게 공로를 돌리기 위해 제공됩니다. 연구에서 VoxCity를 사용할 때 이들을 인용해 주시기 바랍니다.

## 주요 클래스 및 함수

### 생성 모듈 (Generator Module)
- `get_voxcity`: 복셀 도시 모델 생성을 위한 메인 함수
- 건물 데이터 소스: OpenStreetMap {cite}`openstreetmap_2023`, EUBUCCO {cite}`brussee_2023_eubucco`, Overture Maps {cite}`li_2023_overture`, Microsoft Building Footprints, OpenBuilding 2.5D {cite}`wang_2023_openbuilding`
- 토지 피복 데이터 소스: UrbanWatch {cite}`liu_2023_urbanwatch`, ESA WorldCover {cite}`esa_2021_worldcover`, ESRI Land Cover {cite}`lang_2023_esri_landcover`, Dynamic World {cite}`potapov_2022_dynamic_world`, OpenStreetMap {cite}`openstreetmap_2023`
- 수관 높이(Canopy height) 데이터 소스: High Resolution 1m Global Canopy Height Maps {cite}`lang_2023_global_canopy_height`, ETH Global Sentinel-2 10m {cite}`schug_2023_eth_canopy_height`
- 수치 표고 모델(DEM) 데이터 소스: DeltaDTM {cite}`hawker_2022_deltadtm`, FABDEM {cite}`hawker_2022_fabdem`, NASA {cite}`nasadem_2019`, COPERNICUS

### 다운로더 모듈 (Downloader Module)
- `OSMDownloader`: OpenStreetMap 건물 데이터 다운로더 {cite}`openstreetmap_2023`
- `EUBUCCODownloader`: EUBUCCO 건물 데이터 다운로더 {cite}`brussee_2023_eubucco`
- `OvertureDownloader`: Overture Maps 건물 데이터 다운로더 {cite}`li_2023_overture`
- `GEEDownloader`: Google Earth Engine 데이터 다운로더 {cite}`google_earth_engine_2023`

### 엑스포터 모듈 (Exporter Module)
- `ENVIMETExporter`: ENVI-met 시뮬레이션 파일 내보내기 {cite}`envi_met_2020`
- `MagicaVoxelExporter`: MagicaVoxel 복셀 파일 내보내기 {cite}`magicavoxel_2020`
- `OBJExporter`: OBJ 3D 모델 파일 내보내기

### 시뮬레이터 모듈 (Simulator Module)
- `SolarSimulator`: 태양 복사 분석 클래스
- `ViewSimulator`: 가시 지수 및 가시성 분석 클래스

### 지오프로세서 모듈 (Geoprocessor Module)
- `GridProcessor`: 그리드 기반 데이터 처리 클래스
- `MeshProcessor`: 메쉬 생성 및 처리 클래스
- `PolygonProcessor`: 폴리곤 연산 클래스

## 참고문헌 목록

```{bibliography}
```
