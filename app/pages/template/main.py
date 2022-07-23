from models.leaderboard import LeaderboardModel
from views.page_base import PageBase
from views import tab_leaderboard
from views.tab_leaderboard import TabLeaderboard
from . import tab_data
from .tab_data import TabData
from . import tab_description
from .tab_description import TabDescription


_TITLE = 'Test1'


class Test1(PageBase):
    def __init__(self):
        super().__init__()
        self._title = _TITLE
        self._tab_info = [
            {'title': tab_description.TITLE, 'get': TabDescription()},
            {'title': tab_data.TITLE, 'get': TabData()},
            {'title': tab_leaderboard.TITLE, 'get': TabLeaderboard(self._title, LeaderboardModel(self._title))}
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
        return self._tab_info[idx]['get'].get_view()

    def get_tab_title(self, idx):
        return self._tab_info[idx]['title']

