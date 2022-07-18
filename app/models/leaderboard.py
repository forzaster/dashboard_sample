from .local import leaderboard as local_model

from config import Config

# TODO from external DB
_model = local_model if Config.is_local_test else None

def get(title):
    df = _model.get(title)
    df = df.sort_values('score', ascending=False).reset_index(drop=True)
    df['score'] = df['score'].map(lambda x: round(x, 3))
    return df

def put(title, user, score):
    _model.put(title, user, score)
