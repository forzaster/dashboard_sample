import datetime
import random

import pandas as pd


_user_num = 100
_now = datetime.datetime.now()
_now = datetime.datetime(year=_now.year, month=_now.month, day=_now.day)
_df = pd.DataFrame({
    'user': [f'{i:05}' for i in range(_user_num)],
    'score': [random.random() for i in range(_user_num)],
    'date': [_now - datetime.timedelta(days=random.randint(0, 30)) for i in range(_user_num)]
})
_df['date'] = _df['date'].map(lambda x: f'{x:%Y-%m-%d}')

def get(title):
    return _df.copy()

def put(title, user, score):
    d = datetime.datetime.now()
    d = datetime.datetime(year=d.year, month=d.month, day=d)
    _df.append({'user': user, 'score': score, 'date': f'{d:%Y-%m-%d}'}, ignore_index=True)