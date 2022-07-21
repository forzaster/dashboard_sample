from .local import leaderboard as local_model

from config import Config


class LeaderboardModel:
    def __init__(self, title):
        self.title = title

        # TODO from external DB
        self._model = local_model if Config.is_local_test else None

    def get(self):
        df = self._model.get(self.title)
        df = df.sort_values('score', ascending=False).reset_index(drop=True)
        df['score'] = df['score'].map(lambda x: round(x, 3))
        return df

    def put(self, user, score):
        self._model.put(self.title, user, score)
    
    def get_title(self):
        return self.title
