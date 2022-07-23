from dash import html

from views.page_base import PageBase

_TITLE = 'Test2'
_TAB_INFO = [
    {'title': 'Description', 'get': None},
    {'title': 'Data', 'get': None},
    {'title': 'Leaderboard', 'get': None},
]


class Test2(PageBase):
    def __init__(self):
        super().__init__()

    def title(self):
        return _TITLE

    def deadline(self):
        return '2021/12/1'

    def sub_title(self):
        return 'sub test2'

    def background_image(self):
        return 'test2/test2_background.png'

    def get_tab_num(self):
        return 3

    def get_tab(self, idx):
        if func := _TAB_INFO[idx]['get']:
            return func.get_view()
        return html.Div(f'Under construction {idx}')

    def get_tab_title(self, idx):
        return _TAB_INFO[idx]['title']
