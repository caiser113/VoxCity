# 건물 표면 구역(Building Surface Zones) 설계 사양서

**날짜:** 2026-05-05
**상태:** 초안
**범위:** `app/` (FastAPI 백엔드 + React 프런트엔드)

---

## 1. 목표

기존의 2D 영역 기반 조닝(Zoning)을 확장하여 사용자가 3D 뷰어에서 개별 건물 표면(면)을 선택하고 이를 명명된 구역으로 묶을 수 있도록 합니다. 이러한 표면 구역은 지면 기반 시뮬레이션 결과가 아닌 건물 표면 시뮬레이션 결과(Solar, View, Landmark)에 대해 통계 요약을 생성하는 데 사용됩니다.

## 2. 사용자 스토리

1. *건축가로서,* 건물 표면 Solar 시뮬레이션을 실행한 후, 특정 건물의 남측 입면 전체를 선택하고 이를 "South Facade" 구역으로 저장합니다. 해당 입면의 평균 일사량을 즉시 확인합니다.
2. *계획가로서,* 여러 건물의 지붕을 선택하고 이를 "Potential Solar Roofs"로 그룹화하여 해당 표면들에 대한 총 에너지 잠재량 요약을 확인합니다.
3. *연구자로서,* Zoning 탭에서 2D 지면 구역과 3D 건물 표면 구역을 혼합하여 관리하며, 각 시뮬레이션 유형에 맞는 통계 테이블을 확인합니다.

## 3. 데이터 모델 확장

### 3.1 프런트엔드 (`app/frontend/src/types/zones.ts`)

`Zone` 인터페이스에 선택적 `face_ids` 필드를 추가합니다.

```ts
export type ZoneType = 'area' | 'surface';

export interface Zone {
  id: string;
  name: string;
  color: string;
  type: ZoneType;
  // 영역 구역용 (type === 'area')
  ring_lonlat?: [number, number][];
  // 표면 구역용 (type === 'surface')
  face_ids?: number[]; 
}
```

### 3.2 백엔드 (`app/backend/models.py`)

백엔드 모델을 일치하도록 업데이트합니다.

```python
class ZoneSpec(BaseModel):
    id: str
    name: str
    type: str                           # "area" | "surface"
    ring_lonlat: list[list[float]] | None
    face_ids: list[int] | None
```

## 4. 아키텍처 결정

| 결정 사항 | 선택 | 근거 |
| --- | --- | --- |
| 선택 방식 | 3D 뷰어에서 클릭으로 면 선택 | 건물 표면 데이터의 비정형 특성상 2D 지도보다 3D에서 직접 선택하는 것이 가장 직관적입니다. |
| 데이터 저장 | `face_ids` (메시 내 인덱스) 저장 | 현재 세션 내에서 가장 효율적입니다. (참고: 모델 재생성 시 메시 인덱스가 변경될 수 있으므로, v1에서는 모델 변경 시 구역을 지웁니다.) |
| 통계 계산 | 면적 가중 평균 (Area-weighted Mean) | 건물 표면의 면 크기가 일정하지 않으므로, 정확한 물리적 통계를 위해 면적 가중치가 필수적입니다. |

## 5. 구현 세부 사항

### 5.1 프런트엔드: 표면 선택 로직

- **Zoning 탭**에 "Surface Selection" 모드를 추가합니다.
- 사용자가 3D 뷰어에서 건물을 클릭하면 해당 면(face)의 인덱스를 획득합니다.
- `Shift+클릭`으로 다중 선택 또는 선택 해제를 지원합니다.
- 선택된 면들은 3D 뷰어에서 강조 표시(highlight)됩니다.

### 5.2 백엔드: 통계 집계 (`app/backend/zoning.py`)

`surface` 유형의 구역에 대해:
1. `app_state.last_sim_mesh`에서 `face_ids`에 해당하는 데이터 값을 추출합니다.
2. 각 면의 면적(`areas`)을 가중치로 사용하여 평균을 계산합니다.
3. 유효하지 않은 값(NaN/Inf)은 계산에서 제외합니다.

## 6. UI/UX 디자인

- **왼쪽 패널:** 구역 리스트에서 영역 구역과 표면 구역을 아이콘으로 구분하여 표시합니다.
- **도구 모음:** "Draw Area (2D)"와 "Select Surfaces (3D)" 버튼을 제공합니다.
- **통계 테이블:** 현재 시뮬레이션 결과와 일치하는 유형의 구역만 테이블에 표시하거나, 관련 없는 유형은 "N/A" 또는 빈 값으로 처리합니다.
