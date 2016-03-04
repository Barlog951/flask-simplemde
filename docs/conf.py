# -*- coding: utf-8 -*-
#
# Flask-SimpleMDE documentation build configuration file, created by
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, PROJECT_DIR)
import flask_simplemde  # noqa

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'

master_doc = 'index'

project = u'Flask-SimpleMDE'
copyright = u'2016, Philip Xu'
author = u'Philip Xu'

release = flask_simplemde.__version__
version = release.rsplit('.', 1)[0]

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'alabaster'
html_theme_options = {
    'github_banner': True,
    'github_repo': 'flask-simplemde',
    'github_user': 'pyx',
}

htmlhelp_basename = 'Flask-SimpleMDEdoc'

latex_documents = [
    (master_doc, 'Flask-SimpleMDE.tex', u'Flask-SimpleMDE Documentation',
     u'Philip Xu', 'manual'),
]

man_pages = [
    (master_doc, 'flask-simplemde', u'Flask-SimpleMDE Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Flask-SimpleMDE', u'Flask-SimpleMDE Documentation',
     author, 'Flask-SimpleMDE', 'One line description of project.',
     'Miscellaneous'),
]
