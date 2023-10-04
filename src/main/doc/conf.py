# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys
from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bookshelf 1'
year = datetime.now().year
copyright = u"%d, Lyd by Dissing ApS" % year
author = 'Tue Dissing'
release = 'v0.1'

# Sphinx PCB Draw
#sys.path.append(os.path.abspath("../dependencies/sphinx-pcbdraw/sphinx_pcbdraw"))


# Provide a GitHub API token:
# Pass the SPHINX_GITHUB_CHANGELOG_TOKEN environment variable to your build
# OR
# sphinx_github_changelog_token



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'rst2pdf.pdfbuilder',
    'sphinx_charts.charts',
    #'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    #'sphinx-favicon',
    #'sphinxcontrib.youtube',
    'sphinx_panels',
    'myst_parser',
    'sphinxemoji.sphinxemoji',
    'sphinx_last_updated_by_git',
    'sphinx_github_changelog',
    #'sphinx-pcbdraw',
    #'sphinx_ext_substitution',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
# Material theme options (see theme.conf for more information)
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Bookself 1 | an Open Source Analouge Speaker',

    # Set you GA account ID to enable tracking
#    'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://lydbydissing.github.io/bookshelf-1/',

    # Set the color and the accent color
    'theme_color': '1e9944',
    'color_primary': 'green',
    'color_accent': 'light-green',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/LydByDissing/bookshelf-1',
    'repo_name': 'bookshelf-1',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,

 #   'html_minify': True,
#    'css_minify': True,
}
html_logo = '_static/logo-white.svg'
html_static_path = ['_static']
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}