from dash import dcc, html, dash_table
import plotly.express as px
from models.leaderboard import LeaderboardModel

TITLE = 'Leaderboard'

_style={
    'padding-top': '1rem',
    'padding-right': '5rem',
    'padding-left': '1rem',
    'padding-bottom': '2rem'
}

_style_cell = {
    'padding': '0.4rem',
    'textAlign': 'left'
}

_style_header = {
    'padding': '0.4rem',
    'color': 'white',
    'textAlign': 'left',
    'fontWeight': 'bold',
    'backgroundColor': 'gray'
}

_style_data = {
    'padding': '0.4rem',
    'textAlign': 'left'
}


def _create_submission_view(title):
    button_id = f'{TITLE}_submit_button'
    return html.Div([html.H3('Submission'),
                     html.Button('Submit', id=button_id, className='common_button')])

def create(model: LeaderboardModel):
    title = model.get_title()
    df = model.get()
    columns = df.columns.copy()
    df['rank'] = df.index
    df['rank'] = df['rank'] + 1
    df = df[['rank', *columns]]

    fig = px.bar(df[:100], x='user', y='score')
    fig.update_layout(title='High Ranking Score View')
    graph = dcc.Graph(figure=fig)
    table = dash_table.DataTable(id=f'{title}_leaderboard',
                                 columns=[{'name': c, 'id': c} for c in df.columns],
                                 data=df[:100].to_dict('records'),
                                 style_cell=_style_cell,
                                 style_header=_style_header,
                                 style_data=_style_data,
                                 style_cell_conditional=[
                                    {'if': {'column_id': 'rank'}, 'width': '3rem'},
                                    {'if': {'column_id': 'user'}, 'width': '70%'},
                                    {'if': {'column_id': 'score'}, 'width': '5rem'},
                                    {'if': {'column_id': 'Date'}, 'width': '5rem'}])
    return html.Div([_create_submission_view(title),
                     html.H3(f'Ranking'),
                     html.Div([table], style=_style),
                     graph])
