from dash import html, dcc

from config import Config

def _create_tab_item(label, value):
    return dcc.Tab(label=label, value=value, className='sidebar_item',
                   selected_className='sidebar_item_selected')

def _create_tabs(pages):
    tabs = [_create_tab_item(label=pages[i].title(), value=f'{i}') for i in range(len(pages))]
    return dcc.Tabs(id='sidebar_tabs', value='0', children=tabs, vertical=True,
                    style={'width': '100%'}, parent_style={'width': '100%'})

def get_view(width, pages):
    style = {'width': f'{width}rem'}

    children = [html.H2(Config.sidebar_title, className="class_sidebar"),
                _create_tabs(pages)]

    return html.Div(children, className='sidebar', style=style)