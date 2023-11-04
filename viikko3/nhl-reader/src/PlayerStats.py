
class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        self.players.sort(key=lambda x: getattr(x, 'goals') + getattr(x, 'assists'), reverse=True)
        ret = filter(lambda x: getattr(x, 'nationality') == nationality, self.players)
        return ret

