from dash import html, callback, Input, Output

from . import pages as callbacks_pages

def _register_callback(pages):
    @callback(Output(f'contents_container', 'children'),
              Input(f'sidebar_tabs', 'value'))
    def render_page(value):
        idx = int(value)
        p = pages[idx]
        view = p.get_view()
        return view

def register_callbacks(pages):
    _register_callback(pages)
