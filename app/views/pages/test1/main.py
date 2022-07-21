from dataclasses import dataclass

from models.leaderboard import LeaderboardModel
from ...page import PageBase
from .. import tab_leaderboard
from . import tab_data
from . import tab_description


_TITLE = 'Test1'


class Test1(PageBase):
    def __init__(self):
        super().__init__()
        self._title = _TITLE
        self._tab_info = [
            {'title': tab_description.TITLE, 'create': tab_description.get_view, 'args': {}},
            {'title': tab_data.TITLE, 'create': tab_data.create, 'args': {}},
            {'title': tab_leaderboard.TITLE, 'create': tab_leaderboard.create, 'args': {'model': LeaderboardModel(self.title)}}
        ]

    def title(self):
        return self._title

    def deadline(self):
        return '2022/2/1'

    def sub_title(self):
        return 'test1 description, detail and so on.'

    def background_image(self):
        return 'test1/test1_background.png'

    def get_tab_num(self):
        return len(self._tab_info)

    def get_tab(self, idx):
        idx = int(idx)
        args = self._tab_info[idx]['args']
        return self._tab_info[idx]['create'](**args)

    def get_tab_title(self, idx):
        return self._tab_info[idx]['title']

