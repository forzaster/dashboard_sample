from dash import html
from ...page import PageBase
from ...utils import decorator


_TAB_INFO = [
    {'title': 'Description', 'create': None},
    {'title': 'Data', 'create': None},
    {'title': 'Leaderboard', 'create': None},
]


class Test2(PageBase):
    def __init__(self):
        super().__init__()

    def title(self):
        return 'Test2'

    def deadline(self):
        return '2021/12/1'

    def sub_title(self):
        return 'sub test2'

    def background_image(self):
        return 'test2/test2_background.png'

    def get_tab_num(self):
        return 3

    def get_tab_view(self, idx):
        return decorator.rounded(html.Div(f'Under construction {idx}'))

    def get_tab_title(self, idx):
        return _TAB_INFO[idx]['title']
