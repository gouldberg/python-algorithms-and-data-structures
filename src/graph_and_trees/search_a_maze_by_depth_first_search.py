# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import os
from numpy import loadtxt

import collections


# ----------------------------------------------------------------------------
# Search a maze
# recursive DFS (Depth-First Search)
# Time complexity O(|V| + |E|)

# note: BFS (Breadth-First Search) three has the property that the computed path will be
# a shortest path from the entrance.
# However BRS is more difficult to implement than DFS since in DFS, the complier implicitly
# handles the DFS stack, whereas in BFS, the queue has to be explicitly coded.
# ----------------------------------------------------------------------------

def search_maze(maze, s, e):

    # Perform DFS to fine a feasible path.
    def search_maze_helper(cur):

        # Checks cur is within maze and is a white pixel.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and
            maze[cur.x][cur.y] == WHITE):

            return False

        path.append(cur)
        maze[cur.x][cur.y] = BLACK

        if cur == e:
            return True

        if any(
            map(search_maze_helper,
                map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
                    (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True

        # Cannot find a path, remove the entry added in path.append(cur).
        del path[-1]
        return False

    path = []
    search_maze_helper(s)
    return path


# ----------
# load maze data

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure'

maze_array = loadtxt(os.path.join(base_path, '01_data\\search_maze_data.txt'), comments='#', delimiter='\t', unpack=False)

WHITE, BLACK = range(2)


# ----------
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

# But it is not shortest path
print(search_maze(maze=maze_array, s=Coordinate(9,0), e=Coordinate(0,9)))


# ----------
cur = Coordinate(9,0)

print((cur.x - 1, cur.x + 1, cur.x, cur.x))
print((cur.y, cur.y, cur.y - 1, cur.y + 1))

any(map(search_maze_helper,
    map(Coordinate,
    (cur.x - 1, cur.x + 1, cur.x, cur.x),
    (cur.y, cur.y, cur.y - 1, cur.y + 1))))



