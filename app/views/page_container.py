from dash import html

class PageContainer:
    def __init__(self, margin_left):
        self._margin_left = margin_left

    def get_view(self):
        page_margin = 2
        style = {
            "margin-left": f"{self._margin_left+page_margin}rem",
            "padding-left": f"{page_margin}rem",
            "margin-right": f"{page_margin}rem",
            "padding-top": f"{page_margin}rem"
        }
        return html.Div([], id='page_container', style=style)

