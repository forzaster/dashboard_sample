
from dash import dcc, html
import dash_bootstrap_components as dbc

TITLE = 'Data'


def create():
    button_id = f'{TITLE}_download_button'
    button_id_s = f'{TITLE}_submit_button'
    tab = html.Div([html.Div('This is test data.'),
                    html.Button('Download', id=button_id, className='download_button'),
                    html.Button('Submit', id=button_id_s, className='download_button')])

    return tab


