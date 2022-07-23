
from dash import dcc, html
import dash_bootstrap_components as dbc

TITLE = 'Data'


class TabData:
    def get_view(self):
        button_id = f'{TITLE}_download_button'
        tab = html.Div([html.Div('This is test data.'),
                        html.Button('Download', id=button_id, className='common_button')])

        return tab


