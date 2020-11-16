# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Juan Zamora O.'
copyright = '2020, j.z.o.'
author = 'j.z.o.'
html_title = "Juan Zamora O."

# The full version, including alpha/beta/rc tags
release = '1.0'

# Good tutorial
# https://blog.shichao.io/2013/03/19/create_a_personal_website_with_sphinx.html
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'nature'

#html_sidebars = {'**':['localtoc.html','searchbox.html']}
#html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "logo01.jpg"
#html_style = "mystyle.css"
pygments_style = 'sphinx'
#html_theme = 'sphinxdoc'
#html_theme = 'insegel' # muy bueno
#html_theme = 'renku' # igual buioen

html_theme = 'sunpy'
import sunpy_sphinx_theme
html_theme_path = sunpy_sphinx_theme.get_html_theme_path()

#import sphinx_redactor_theme
#html_theme = 'sphinx_redactor_theme'
#html_theme_path = [sphinx_redactor_theme.get_html_theme_path()]

html_theme_options = {
    'description': 'ABCDE.',
    'github_repo': 'jfzo',
    'nosidebar': False,
    'header_searchbox': False,
    'rightsidebar': False,
}
todo_include_todos = False
html_use_index = False
html_sidebars = {}
html_show_sourcelink = False