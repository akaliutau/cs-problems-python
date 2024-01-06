from collections import Counter
from collections import OrderedDict


class Player:

    def __init__(self, idx, name, games, score):
        self.idx = idx
        self.name = name
        self.games = games
        self.score = score

    def __lt__(self, oth):
        if self.score > oth.score:
            return True
        elif self.score < oth.score:
            return False

        if self.games < oth.games:
            return True
        elif self.games > oth.games:
            return False

        if self.idx < oth.idx:
            return True
        elif self.idx > oth.idx:
            return False


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        ord_li = []
        idx = 0
        for player, res in self.standings.items():
            ord_li.append(Player(idx, player, res['games_played'], res['score']))
            idx += 1
        ord_li.sort()
        return ord_li[rank - 1].name


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))

