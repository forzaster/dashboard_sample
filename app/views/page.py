from abc import abstractmethod
from dash import html, dcc

from models import asset_manager

_page_margin = 2


class PageBase:
    def __init__(self):
        self.content = None

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def background_image(self):
        pass

    @abstractmethod
    def get_tab_view(self, n):
        pass

    @abstractmethod
    def get_tab_title(self, n):
        pass

    @abstractmethod
    def get_tab_num(self):
        pass

    def tab_id(self):
        return f'tabs_{self.title()}'

    def tab_container_id(self):
        return f'tabs_{self.title()}_container'

    def _create_title(self):
        title = self.title()
        bg_image = asset_manager.get(self.background_image())
        title_style = {
            'background-image': f'url("{bg_image}")',
            'background-size': 'cover',
            'color': 'white',
            'padding': '1rem'
        } if bg_image else {}
        return html.Div([html.H1(title),
                         html.Div(self.description(), style={"margin": "1rem"})],
                         style=title_style)

    def _create_tab_item(self, label, value):
        return dcc.Tab(label=label, value=value, className='tab_item', selected_className='tab_item_selected')

    def _create_tabs(self):
        return dcc.Tabs(id=self.tab_id(), value='0', children=[
                        self._create_tab_item(label=self.get_tab_title(i), value=f'{i}')
                         for i in range(self.get_tab_num())])

    def _create_tabs_container(self):
        return html.Div(id=self.tab_container_id())

    def _create(self):
        return html.Div([self._create_title(),
                         self._create_tabs(),
                         self._create_tabs_container()])

    def get_view(self):
        if self.content is None:
            self.content = self._create()
        return self.content


def get_page_root_view(margin_left, page):
    style = {
        "margin-left": f"{margin_left+_page_margin}rem",
        "padding-left": f"{_page_margin}rem",
        "margin-right": f"{_page_margin}rem",
        "padding-top": f"{_page_margin}rem"
    }
    page_view = page.get_view()
    return html.Div([page_view], id='contents_container', style=style)
