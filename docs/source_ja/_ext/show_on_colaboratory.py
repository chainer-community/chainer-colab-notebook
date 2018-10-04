"""
Sphinx extension to add ReadTheDocs-style "Show on Colaboratory" links to the
sidebar.
Loosely based on https://github.com/astropy/astropy/pull/347
"""

import os
import warnings


__licence__ = 'BSD (3 clause)'


def get_colaboratory_url(path):
    fromto = [('hands_on', 'hands_on_ja'), ('official_example', 'official_example_ja')]
    for f, t in fromto:
        if path.startswith(f):
            path = path.replace(f, t, 1)
    return 'https://colab.research.google.com/github/chainer-community/chainer-colab-notebook/blob/master/{path}'.format(
        path=path)


def html_page_context(app, pagename, templatename, context, doctree):
    path = os.path.relpath(doctree.get('source'), app.builder.srcdir).replace('notebook/', '')
    show_url = get_colaboratory_url(path)

    context['show_on_colaboratory_url'] = show_url


def setup(app):
    app.connect('html-page-context', html_page_context)
