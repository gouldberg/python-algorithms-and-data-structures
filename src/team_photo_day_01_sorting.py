# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import collections


# ----------------------------------------------------------------------------
# team photo day
#  - You are a photographer for a soccer meet. You will be taking pictures of pairs of opposing teams.
#    All teams have the same number of players. A team photo consists of a front row of players
#    and a back row of players. A player in the back row must be taller than the player in front of him.
#    All players in a row must be from the same team
#  - sorting
#  - time complexity:  O(n * log(n))
# ----------------------------------------------------------------------------

class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks of team0 can be placed in front of team1
    @staticmethod
    def valid_placement_exists(team0, team1):
        return all(a < b for a, b in zip(sorted(team0._players), sorted(team1._players)))


# ----------

team0_height = [10, 20, 30, 40, 60, 80]
team0 = Team(team0_height)
print(team0._players)

team1_height = [20, 30, 40, 60, 80, 100]
team1 = Team(team1_height)
print(team1._players)

Team.valid_placement_exists(team0, team1)
