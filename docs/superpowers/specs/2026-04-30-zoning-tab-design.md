# Zoning(조닝) 탭 — 설계 사양서

**날짜:** 2026-04-30
**상태:** 초안 (구현 전)
**범위:** `app/` (FastAPI 백엔드 + React 프런트엔드)

---

## 1. 목표

VoxCity 웹 앱에 **Zoning(조닝)** 탭을 추가하여 사용자가 현재 모델 위에 하나 이상의 2D 풋프린트(footprint) 구역을 정의할 수 있도록 합니다. 이후의 각 시뮬레이션 탭(Solar, View, Landmark)은 캐시된 결과로부터 계산된 구역별 요약 통계와 모델 뷰어에서의 각 구역에 대한 3D 외곽선을 표시합니다.

## 2. 비목표 (v1)

- 3D 볼륨 구역 (구역별 z-min / z-max)
- 구역 그룹화를 위한 카테고리 / 태그
- 건물 그룹 구역 (건물 풋프린트를 선택하여 정의된 구역)
- 구역별 히스토그램 또는 백분위수 통계
- 구역의 백엔드 지속성 (페이지 새로고침 또는 재시작 시 유지되지 않음)
- GeoJSON / Shapefile에서 구역 가져오기
- 오클루더(occluder)를 통한 실제 "항상 위에 표시(always-on-top)" 렌더링 (Plotly 제한 사항)

이러한 항목들은 의도적으로 연기되었으며, 데이터 모델은 v1 계약을 깨지 않고 나중에 추가할 수 있는 여지를 남겨둡니다.

## 3. 사용자 스토리

1. *연구자로서,* 모델을 생성한 후 **Zoning** 탭을 열고, 중정 주위에 회전된 직사각형을 그리고 거리 위를 따라 폴리곤을 그립니다. 2D 지도에 외곽선으로 표시된 두 구역과 3D 뷰어에서 유색 수직 커튼으로 표시된 구역을 확인합니다.
2. *일사량(Solar) 시뮬레이션을 실행합니다.* Solar 탭의 실행 컨트롤 아래에서 각 구역에 대한 일사량의 `count, mean, min, max, std`가 포함된 테이블을 확인하고, 색상이 입혀진 3D 결과 위에 그려진 동일한 구역 외곽선을 확인합니다.
3. *Zoning 탭에서 구역을 수정합니다* (이름 변경, 색상 변경, 삭제, 새 구역 그리기). 다시 Solar 탭으로 돌아오면 시뮬레이션을 재실행하지 않고도 기존 결과에 대해 테이블이 새로 고쳐집니다.
4. *Target Area 탭에서 대상 영역을 변경합니다* — 내 구역들이 삭제됩니다 (다른 지역에 속해 있었기 때문).

## 4. 아키텍처 결정

| 결정 사항 | 선택 | 근거 |
| --- | --- | --- |
| 구역 형상 | 2D 폴리곤 풋프린트 (높이 범위 없음) | 지배적인 사용 사례를 충족하는 가장 단순한 모델이며, 기존의 `last_sim_grid` / `last_sim_mesh` 캐시에 대해 깔끔하게 집계됩니다. |
| 그리기 기본 도형 | 회전된 직사각형 (기본값) + 폴리곤 | `PlanMapEditor`의 기존 `EditTab` 건물 그리기 기본 도형과 일치합니다. 새로운 기본 도형이 필요하지 않습니다. |
| 다중 구역 | 평면 리스트, 자동 명명 "Zone N", 중첩 허용 | 앱의 나머지 부분과 일치합니다. 카테고리는 필요성 근거 없이 UI 무게만 가중시킵니다. |
| 지속성 | `App.tsx`의 프런트엔드 상태, 경위도(lon/lat) 폴리곤 | 편집/생성 재실행 시에도 유지됩니다. 대상 직사각형이 변경되면 삭제됩니다. 기존 패턴(`rectangle`, `figureJson`, 편집 버퍼)을 반영합니다. |
| 통계 계산 | 새로운 상태 비저장(stateless) `POST /api/zones/stats` | 단일 엔드포인트; 시뮬레이션 핸들러는 건드리지 않음; "시뮬레이션 재실행 없이 구역 편집"을 지원합니다. |
| 탭 순서 | `Area · Generation · Edit · Zoning · Solar · View · Landmark · Export` | 자연스러운 흐름; 다른 모델 이후 탭과 동일한 `hasModel` 게이팅을 적용합니다. |
| 레이아웃 | `.three-col` 쉘 (설정 \| 2D 편집기 \| 3D 뷰어) | `EditTab`을 반영합니다. |

## 5. 데이터 모델

### 5.1 프런트엔드 (`app/frontend/src/types/zones.ts`, 신규)

```ts
export type ZoneShape = 'rect' | 'polygon';

export interface Zone {
  id: string;                          // uuid (클라이언트 생성)
  name: string;                        // 기본값 "Zone 1"; 사용자 편집 가능
  color: string;                       // 기본 팔레트의 헥사 코드; 사용자 편집 가능
  shape: ZoneShape;                    // 정보용
  ring_lonlat: [number, number][];     // [[lon, lat], ...], 닫히지 않음
}
```

`rectangle` / `figureJson` 옆의 `App.tsx`로 상태가 끌어올려짐:

```ts
const [zones, setZones] = useState<Zone[]>([]);
```

기존의 UX 버그(캐시된 시뮬레이션 수치가 다음 `/generate`까지 대상 직사각형 변경 시에도 유지되는 문제)를 해결하는 명시적인 효과와 연결됨:

```ts
// 대상 직사각형이 변경될 때 구역과 캐시된 시뮬레이션 수치를 모두 지웁니다.
// 이전 결과는 더 이상 새 영역과 일치하지 않습니다.
useEffect(() => {
  setZones([]);
  setFigureJson('');
  setEditFigureJson('');
  setSolarFigureJson('');
  setViewFigureJson('');
  setLandmarkFigureJson('');
}, [rectangle]);
```

그 후 `zones`는 `<ZoningTab>`, `<SolarTab>`, `<ViewTab>`, `<LandmarkTab>`에 읽기 전용으로 전달됩니다.

### 5.2 백엔드 (`app/backend/models.py`)

```python
class ZoneSpec(BaseModel):
    id: str
    name: str
    ring_lonlat: list[list[float]]      # [[lon, lat], ...] (3개 이상의 점)

class ZoneStatsRequest(BaseModel):
    zones: list[ZoneSpec]

class ZoneStat(BaseModel):
    zone_id: str
    cell_count: int
    valid_count: int                    # 유한한 값을 가진 셀/면의 수
    mean: float | None
    min:  float | None
    max:  float | None
    std:  float | None

class ZoneStatsResponse(BaseModel):
    target:     str                     # "ground" | "building" | "none"
    sim_type:   str | None              # "solar" | "view" | "landmark" | None
    unit_label: str | None              # AppState.last_colorbar_title을 반영
    stats:      list[ZoneStat]
```

서버 측 구역 상태는 없으며, 기존의 `AppState.last_sim_*` 캐시를 재사용합니다.

## 6. 백엔드 엔드포인트

### 6.1 라우트

`POST /api/zones/stats` → `ZoneStatsResponse`

### 6.2 핸들러 개요

```python
@app.post("/api/zones/stats", response_model=ZoneStatsResponse)
def zone_stats(req: ZoneStatsRequest):
    if app_state.voxcity is None:
        raise HTTPException(400, "모델이 로드되지 않았습니다")
    if app_state.last_sim_type is None:
        raise HTTPException(400, "시뮬레이션을 먼저 실행하십시오")
    if app_state.last_sim_target == "ground":
        return _zone_stats_ground(req.zones)
    if app_state.last_sim_target == "building":
        return _zone_stats_building(req.zones)
    raise HTTPException(400, f"지원되지 않는 대상: {app_state.last_sim_target}")
```

### 6.3 집계

**지면(Ground)** — 각 경위도 링을 프런트엔드 `polygonToCells`(`app/frontend/src/lib/grid.ts`에 있음)의 Python 포팅 버전을 통해 그리드 셀로 변환합니다. `app_state.last_sim_grid[i, j]`를 인덱싱하고, 유한하지 않은 값을 제외한 후 `mean/min/max/std`를 계산합니다.

**건물 표면(Building surfaces)** — `app_state.last_sim_mesh`의 각 면에 대해 그리드 로컬 미터 단위의 중심점을 계산하고, 경위도로 투영한 후 각 구역에 대해 점-폴리곤 포함 테스트를 수행합니다. `mean`의 경우 면적 가중(area-weighted) 방식으로 집계하고, `min`, `max`, `std`는 가중치 없이 집계합니다. (면적 가중 방식이 원하는 동작임을 확인했으며, 면 중심점 포함 여부가 원하는 포함 규칙입니다.)

### 6.4 새 모듈

`app/backend/zoning.py`에 다음 기능을 수용합니다:

- `polygon_lonlat_to_cells(ring, grid_geom) -> list[(int, int)]`
- `grid_xy_to_lonlat(xy, grid_geom) -> ndarray`
- `points_in_polygon(points_lonlat, ring) -> ndarray[bool]`
- `_stats_from(zone_id, count, values, mask) -> ZoneStat`

`main.py`를 깔끔하게 유지합니다.

### 6.5 예외 케이스

| 입력 | 응답 |
| --- | --- |
| 빈 `zones` 리스트 | `200`, `stats: []` |
| 그리드 완전히 바깥에 있는 구역 | `cell_count: 0`인 행, 모든 지표 `null` |
| 모든 값이 NaN/inf인 구역 | `valid_count: 0`, 모든 지표 `null` |
| 모델이 로드되지 않음 | `400 모델이 로드되지 않았습니다` |
| 시뮬레이션 캐시 없음 | `400 시뮬레이션을 먼저 실행하십시오` |

## 7. 프런트엔드 — Zoning 탭

**파일:** `app/frontend/src/tabs/ZoningTab.tsx` (신규)

### 7.1 레이아웃 (`.three-col`, `EditTab` 반영)

```
.three-col
├── .panel  (왼쪽)             ← 설정 + 구역 리스트
│   ├── <h2>Zoning</h2>
│   ├── 도구 모음 (모드 + 형상 버튼)
│   ├── 기본 색상 팔레트 표시기
│   ├── ── Zones ──
│   │     ● Zone 1  [✎][🗑]
│   │     ● Zone 2  [✎][🗑]
│   │   [+ 새 구역 추가]   [모두 지우기]
│   └── (정보 / 에러 배너)
│
├── .map-pane  (중앙)        ← <PlanMapEditor>
│   - drawColor   = 활성 그리기 색상 (다음 구역의 색상)
│   - interaction = 'draw_rect_3pt' | 'draw_polygon'
│   - pendingEdits = `paint_zone` 오버레이로 렌더링된 구역들
│
└── .three-pane (오른쪽)        ← <ThreeViewer>
    - Zoning 모드에서 `figureJson`
```
