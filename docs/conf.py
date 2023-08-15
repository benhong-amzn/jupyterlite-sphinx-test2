# -*- coding: utf-8 -*-

extensions = [
    'jupyterlite_sphinx',
    'myst_parser',
]

# html_theme = "pydata_sphinx_theme"
html_theme = "sphinx_rtd_theme"
html_logo = "_static/amz-braket.png"
html_title = "Amazon Braket Python SDK"

jupyterlite_contents = "./custom_contents"
jupyterlite_bind_ipynb_suffix = False

master_doc = 'index'

# General information about the project.
project = 'Amazon Braket SDK'

# theme configuration
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyterlite/jupyterlite-sphinx",
            "icon": "fa-brands fa-github",
        }
    ]
}

suppress_warnings = ["myst.xref_missing"]
