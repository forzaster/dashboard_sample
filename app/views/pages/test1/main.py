
from dataclasses import dataclass

from ...page import PageBase
from ...utils import decorator
from . import tab_description
from . import tab_data
from . import tab_leaderboard


_TAB_INFO = [
    {'title': tab_description.TITLE, 'create': tab_description.create},
    {'title': tab_data.TITLE, 'create': tab_data.create},
    {'title': tab_leaderboard.TITLE, 'create': tab_leaderboard.create},
]

class Test1(PageBase):
    def __init__(self):
        super().__init__()

    def title(self):
        return 'Test1'

    def description(self):
        return 'test1 description, detail and so on.'

    def background_image(self):
        return 'test1/test1_background.png'

    def get_tab_num(self):
        return len(_TAB_INFO)

    def get_tab_view(self, idx):
        tab = _TAB_INFO[int(idx)]['create']()
        return decorator.rounded(tab)

    def get_tab_title(self, idx):
        return _TAB_INFO[idx]['title']

