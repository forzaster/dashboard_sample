from dash import html

def rounded(view):
    return html.Div([html.Div([view],
                              style={'padding': '1rem',
                                     'color': 'dimgray',
                                     'border': '1px solid',
                                     'border-radius': '10px',
                                     'border-color': 'lightgray'})],
                    style={'padding': '1rem'})