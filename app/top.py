from dash import html

from config import Config
from views.sidebar import Sidebar, SidebarItem
from views.page_container import PageContainer
from pages.template.main import PageTemplate
from pages.test2.main import Test2

# contents page definition
_pages = [PageTemplate(),
          Test2()]


class SidebarItemForPage(SidebarItem):
    def __init__(self, page):
        self._page = page
    
    def title(self):
        return f'{self._page.title()} ~ {self._page.deadline()}'

    def get_view(self):
        return self._page.get_view()


def _create_sidebar_items():
    return [SidebarItemForPage(p) for p in _pages]

def create_view():
    page_view = PageContainer(Config.sidebar_width).get_view()
    for p in _pages:
        p.register_callback()

    sidebar = Sidebar(Config.sidebar_title)
    sidebar_view = sidebar.get_view(_create_sidebar_items(), Config.sidebar_width, page_view.id)

    return html.Div([sidebar_view, page_view])
