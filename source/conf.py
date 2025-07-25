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

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "style_nav_header_background": "#003285",  

}

html_static_path = ['_static']

# Add custom CSS for numbering
html_css_files = [
    'custom.css',
]

html_logo = '_static/EF5-01.png'