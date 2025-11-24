# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EF5Manual'
copyright = '2025, AHWA Laboratory, IIHR - Hydroscience & Engineering, University of Iowa'
author = 'Humberto Vergara, Santiago Henao, Naman Mehta'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton',
    'sphinx.ext.autosectionlabel'
]

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 1 

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "style_nav_header_background": "#003285",  

}

# Show a persistent global table of contents in the sidebar and
# control navigation behaviour so the index doesn't change per-page.
html_sidebars = {
    '**': [
        'globaltoc.html',  # full tree for the whole site
        'relations.html',
        'searchbox.html',
    ]
}

# sphinx_rtd_theme options to avoid collapsing sections unexpectedly
html_theme_options.update({
    'collapse_navigation': False,
    'navigation_depth': 3,
    'titles_only': False,
})

html_static_path = ['_static']

# Add custom CSS for numbering
html_css_files = [
    'custom.css',
]

html_logo = '_static/EF5-01.png'

# Add a global warning banner to the bottom of every page
rst_epilog = """
.. warning::
   🚧 This documentation is currently under active development.  
   Content may change frequently and some sections may be incomplete.
"""