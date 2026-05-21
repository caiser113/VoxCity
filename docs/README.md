# VoxCity 문서 (Documentation)

이 디렉토리는 Sphinx를 사용하여 빌드되고 Read the Docs에 배포되는 VoxCity의 문서 소스 파일들을 포함하고 있습니다.

## 로컬 개발 환경 구축

로컬에서 문서를 빌드하는 방법은 다음과 같습니다:

```bash
# 문서 빌드에 필요한 의존성 설치
pip install -r docs/requirements.txt

# API 문서 생성을 위해 패키지를 편집 가능한 모드로 설치
pip install -e .

# 문서 빌드
cd docs
make html

# 문서 확인
# 브라우저에서 docs/_build/html/index.html 파일을 엽니다.
```

## Read the Docs 배포

문서는 저장소 루트에 있는 `.readthedocs.yml` 파일을 사용하여 Read the Docs에서 자동으로 빌드됩니다.

### 주요 설정

- **Python**: 3.12
- **Sphinx 설정**: `docs/conf.py`
- **의존성**: `docs/requirements.txt`
- **출력 형식**: HTML

### 사용자 정의 (Customization)

- **테마**: Furo 테마 사용 (현대적이고 반응형 디자인)
- **로고**: `docs/logo.png`에 있는 사용자 정의 로고 사용
- **스타일링**: `docs/_static/custom.css`에 있는 사용자 정의 CSS 적용
- **API 문서**: `sphinx-autoapi`를 사용하여 자동으로 생성

### 문제 해결 (Troubleshooting)

빌드가 실패할 경우:
1. Read the Docs의 빌드 로그를 확인하세요.
2. 모든 의존성이 `docs/requirements.txt`에 포함되어 있는지 확인하세요.
3. `docs/conf.py`의 Sphinx 설정을 검토하세요.
4. docs 디렉토리에서 `make html`을 실행하여 로컬에서 테스트해 보세요.

## 문서 구조

- `index.md`: 메인 랜딩 페이지
- `example.ipynb`: 빠른 시작 가이드 (myst-nb를 통해 렌더링됨)
- `examples/`: 튜토리얼 예제들
- `autoapi/`: 자동 생성된 API 문서
- `references.bib`: 인용을 위한 참고문헌 목록

## 문서 브랜치 배포

GitHub Actions 워크플로우(`.github/workflows/docs.yml`)를 통해 빌드된 HTML을 `documentation` 브랜치에 게시하여 GitHub Pages로 서비스하거나 아카이브할 수 있습니다.

### 수동 배포 (선택 사항)

수동으로 배포해야 하는 경우:

1. 문서를 빌드합니다:
   ```bash
   make html
   ```

2. 빌드된 파일은 `_build/html/` 디렉토리에 생성됩니다.

3. documentation 브랜치로 배포합니다:
   ```bash
   cd docs/_build/html
   git init
   git add -A .
   git commit -m "Update documentation"
   git push -f origin HEAD:documentation
   ```

## 설정

문서 설정은 `conf.py`에서 관리됩니다. 주요 설정:

- 프로젝트 이름: `voxcity`
