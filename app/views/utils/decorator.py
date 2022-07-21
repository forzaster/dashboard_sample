from dash import html

def rounded(func):
    def wrapper(*args,**kwargs):
        view = func(*args,**kwargs)
        return html.Div([html.Div([view],
                        style={'padding': '1rem',
                                'color': 'dimgray',
                                'border': '1px solid',
                                'border-radius': '10px',
                                'border-color': 'lightgray'})],
                        style={'padding': '1rem'})
    return wrapper