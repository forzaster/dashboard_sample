from dash import html, callback, Input, Output

def _register_callback(p):
    title = p.title()
    @callback(Output(f'tabs_{title}_container', 'children'),
              Input(f'tabs_{title}', 'value'))
    def render_tab(tab):
        if tab_content := p.get_tab_view(tab):
            return tab_content
        return html.Div('')

def register_callbacks(pages):
    for p in pages:
        _register_callback(p)
