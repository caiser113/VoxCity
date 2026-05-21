# Sphinx 문서 빌더를 위한 설정 파일입니다.
#
# 이 파일은 가장 일반적인 옵션들만 포함하고 있습니다. 전체 목록은 다음 문서를 참조하세요:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- 프로젝트 정보 -----------------------------------------------------

project = "VoxCity"
copyright = "2024, Kunihiko Fujiwara"
author = "Kunihiko Fujiwara"

# -- 일반 설정 ---------------------------------------------------

# 여기에 Sphinx 확장 모듈 이름을 문자열로 추가합니다. 
# Sphinx에서 제공하는 기본 확장('sphinx.ext.*')이나 사용자 정의 확장을 사용할 수 있습니다.

extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
]

# myst-nb 설정을 위한 라인 추가
nb_execution_mode = "off"

# Bibtex 설정
bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "plain"
autoapi_dirs = ["../src"]

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "imported-members",
    "special-members",
    # "private-members",
    "inherited-members",
    "show-module-summary",
]

autoapi_own_page_level = "class"

# 소스 파일을 찾을 때 무시할 디렉토리와 파일 패턴 목록입니다.
# 이 패턴은 html_static_path와 html_extra_path에도 영향을 줍니다.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML 출력 옵션 -------------------------------------------------

# HTML 및 HTML 도움말 페이지에 사용할 테마입니다. 
# 내장 테마 목록은 문서를 참조하세요.
html_theme = "furo"

# 테마 옵션은 테마별로 다르며 테마의 모양과 느낌을 사용자 정의합니다.
# 각 테마에서 사용 가능한 옵션 목록은 문서를 참조하세요.
html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    # "announcement": "이것은 문서의 베타 버전입니다.",
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
}

html_title = "VoxCity 문서"
# 다음 라인은 제거하거나 주석 처리하세요:
# html_logo = "logo.png"
html_favicon = "_static/favicon.ico"  # 파비콘 파일이 있는지 확인하세요.

# 다른 html_* 설정 근처에 다음 라인들을 추가하세요.
html_static_path = ["_static"]
html_css_files = ["custom.css"]

def skip_util_classes(app, what, name, obj, skip, options):
    # 이 프로젝트는 AutoAPI를 위한 특별한 건너뛰기 로직이 필요하지 않습니다.
    return skip
