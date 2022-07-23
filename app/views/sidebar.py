from abc import abstractmethod
from typing import List

from dash import html, callback, Input, Output, dcc


class SidebarItem:
    @abstractmethod
    def title():
        pass

    @abstractmethod
    def get_view():
        pass


class Sidebar:
    def __init__(self, title: str):
        self._title = title

    def _create_sidebar_item(self, label: str, value: str):
        return dcc.Tab(label=label, value=value, className='sidebar_item',
                    selected_className='sidebar_item_selected')

    def _create_sidebar_item_root(self, items: List[SidebarItem]):
        tabs = [self._create_sidebar_item(label=item.title(), value=f'{i}') for i, item in enumerate(items)]
        return dcc.Tabs(id='sidebar_tabs', value='0', children=tabs, vertical=True,
                        style={'width': '100%'}, parent_style={'width': '100%'})

    def _register_callback(self, items, container_id):
        # callback of select item of sidebar
        @callback(Output(container_id, 'children'),
                Input(f'sidebar_tabs', 'value'))
        def render_page(value):
            idx = int(value)
            return items[idx].get_view()

    def get_view(self, items: List[SidebarItem], width: int, container_id: str):
        style = {'width': f'{width}rem'}
        children = [html.H2(self._title, className="class_sidebar"),
                    self._create_sidebar_item_root(items)]
        view = html.Div(children, className='sidebar', style=style)
        self._register_callback(items, container_id)
        return view