# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import os
from numpy import loadtxt

import collections


# ----------------------------------------------------------------------------
# Paint a Boolean Matrix, Flip Color
# Breadth-First Search
# Time complexity O(m * n)
# ----------------------------------------------------------------------------

def flip_color_bfs(x, y, image_orig):

    image = image_orig.copy()

    color = image[x][y]
    q = collections.deque([(x, y)])

    # flips
    image[x][y] = 1 - image[x][y]

    while q:
        x, y = q.popleft()

        for next_x, next_y in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
                and image[next_x][next_y] == color):

                # flips the color
                image[next_x][next_y] = 1 - image[next_x][next_y]
                q.append((next_x, next_y))

    return image


# ----------
# load boolean matrix

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure'

image = loadtxt(os.path.join(base_path, '01_data\\flip_color_data1.txt'), comments='#', delimiter='\t', unpack=False)


# ----------
# x in vertical (not horizontal !!!)
# y in horizontal
flipped = flip_color_bfs(x=5, y=4, image_orig=image)

flipped2 = flip_color_bfs(x=3, y=6, image_orig=flipped)

print(image)

print(flipped)

print(flipped2)


# ----------------------------------------------------------------------------
# Paint a Boolean Matrix, Flip Color
# Depth-First Search, recursive solution
# Time complexity O(|V| + |E|)
# ----------------------------------------------------------------------------

def flip_color_dfs(x, y, image):

    color = image[x][y]

    # flips
    image[x][y] = 1 - image[x][y]

    for next_x, next_y in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
            and image[next_x][next_y] == color):

            flip_color_dfs(next_x, next_y, image)

    # return image


# ----------
# load boolean matrix

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure'

image = loadtxt(os.path.join(base_path, '01_data\\flip_color_data1.txt'), comments='#', delimiter='\t', unpack=False)

print(image)


# ----------
# x in vertical (not horizontal !!!)
# y in horizontal
flip_color_dfs(x=5, y=4, image=image)

print(image)

flip_color_dfs(x=3, y=6, image=image)

print(image)

