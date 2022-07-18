from dash import html

from callbacks import pages as callbacks_pages
from callbacks import sidebar as callbacks_sidebar
from views import sidebar
from views import page
from views.pages.test1.main import Test1
from views.pages.test2.main import Test2

# contents page definition
_pages = [Test1(),
          Test2()]

# main style
_sidebar_width = 12


def create_view():
    sidebar_view = sidebar.get_view(_sidebar_width, _pages)
    callbacks_sidebar.register_callbacks(_pages)
    p = _pages[0]
    page_view = page.get_page_root_view(_sidebar_width, p)
    callbacks_pages.register_callbacks(_pages)
    return html.Div([sidebar_view, page_view])
