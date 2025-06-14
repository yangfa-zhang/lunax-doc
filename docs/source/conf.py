# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'lunax'
copyright = '2025, yangfa-zhang'
author = 'yangfa-zhang'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = './imgs/luna_logo2.png'
html_logo_width = '20px'  
# -- Options for EPUB output
epub_show_urls = 'footnote'
