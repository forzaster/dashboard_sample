from dataclasses import dataclass

from ...page import PageBase
from ...utils import decorator
from .. import tab_leaderboard
from . import tab_data
from . import tab_description


_TAB_INFO = [
    {'title': tab_description.TITLE, 'create': tab_description.get_view},
    {'title': tab_data.TITLE, 'create': tab_data.create},
    {'title': tab_leaderboard.TITLE, 'create': tab_leaderboard.create},
]

class Test1(PageBase):
    def __init__(self):
        super().__init__()

    def title(self):
        return 'Test1'

    def deadline(self):
        return '2022/2/1'

    def sub_title(self):
        return 'test1 description, detail and so on.'

    def background_image(self):
        return 'test1/test1_background.png'

    def get_tab_num(self):
        return len(_TAB_INFO)

    def get_tab_view(self, idx):
        return decorator.rounded(_TAB_INFO[int(idx)]['create']())

    def get_tab_title(self, idx):
        return _TAB_INFO[idx]['title']

