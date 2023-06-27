# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW -E --keep-going -b html . ./_build/html
#  .venv/bin/sphinx-build  -nW -E --keep-going -b html . ./_build/html
html_favicon = 'favicon.ico'

language = 'en'

# html_static_path = ['_static']

project = 'Tldraw Examples'
# copyright = ''
# author = ''
html_title = "Tldraw Examples"

# specify project details
master_doc = "index"
project = "MyST-NB Quickstart"

# basic build settings
exclude_patterns = ["_build", "README.md"]
include_patterns = ["*.md", "*.ipynb"]


# nb_ipywidgets_js = {
#     "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js": {
#         "integrity": "sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=",
#         "crossorigin": "anonymous",
#     },
#     "https://cdn.jsdelivr.net/npm/@jupyter-widgets/html-manager@*/dist/embed-amd.js": {
#         "data-jupyter-widgets-cdn": "https://cdn.jsdelivr.net/npm/",
#         "crossorigin": "anonymous",
#     },
# }

nitpicky = True

nb_execution_mode = "off"

# load extensions
extensions = ["myst_nb",
              "sphinx_copybutton"
]

html_theme = 'furo'