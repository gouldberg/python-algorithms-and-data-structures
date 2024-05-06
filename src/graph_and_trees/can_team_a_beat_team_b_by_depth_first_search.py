# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import collections


# ----------------------------------------------------------------------------
# can team A beat team B
#  - DFS (depth-first search)
# ----------------------------------------------------------------------------

def can_team_a_beat_team_b(matches, team_a, team_b):

    def build_graph():

        graph = collections.defaultdict(set)

        for match in matches:
            graph[match.winning_team].add(match.losing_team)

        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):

        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)


# ----------
MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))

# directed acyclic graph (DAG)
matches = [
    MatchResult('a', 'b'),
    MatchResult('a', 'c'),
    MatchResult('b', 'k'),
    MatchResult('k', 'i'),
    MatchResult('k', 'f'),
    MatchResult('i', 'j'),
    MatchResult('i', 'l'),
    MatchResult('j', 'l'),
    MatchResult('j', 'f'),
    MatchResult('c', 'e'),
    MatchResult('e', 'd'),
    MatchResult('d', 'f'),
    MatchResult('g', 'f'),
    MatchResult('d', 'h'),
    MatchResult('g', 'h'),
    MatchResult('m', 'n'),
    ]

print(matches)


# ----------
# build_graph

graph = collections.defaultdict(set)

for match in matches:
    graph[match.winning_team].add(match.losing_team)

print(graph)


# ----------
print(can_team_a_beat_team_b(matches=matches, team_a='b', team_b='l'))
