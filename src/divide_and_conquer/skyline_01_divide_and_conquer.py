# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# skyline
# ----------------------------------------------------------------------------

def getSkyline(buildings):
    n = len(buildings)
    # The base cases
    if n == 0:
        return []
    if n == 1:
        x_start, x_end, y = buildings[0]
        return [[x_start, y], [x_end, 0]]

    # ----------
    # If there is more than one building, recursively divide the input into two subproblems
    print('DIVIDE')
    print(f'    left: {buildings[: n // 2]}')
    print(f'    right: {buildings[n // 2:]}')

    left_skyline = getSkyline(buildings[: n // 2])
    right_skyline = getSkyline(buildings[n // 2:])

    # Merge the results of subproblem together
    return merge_skylines(left_skyline, right_skyline)


def merge_skylines(left, right):

    # update the final output with the new element
    def update_output(x, y):
        # if skyline change is not vertical - add the new point
        if not output or output[-1][0] != x:
            output.append([x, y])
        # if skyline change is vertical - update the last point
        else:
            output[-1][1] = y

        print('UPDATE OUTPUT')
        print(f'    {output}')

    # append the rest of the skyline elements with indice (p, n) to the final output
    def append_skyline(p, lst, n, y, curr_y):
        while p < n:
            x, y = lst[p]
            p += 1
            if curr_y != y:
                update_output(x, y)
                curr_y = y

    n_l, n_r = len(left), len(right)
    p_l = p_r = 0
    curr_y = left_y = right_y = 0
    output = []

    # while we're in the region where both skylines are present
    while p_l < n_l and p_r < n_r:
        point_l, point_r = left[p_l], right[p_r]

        # pick up the smallest x
        if point_l[0] < point_r[0]:
            x, left_y = point_l
            p_l += 1
        else:
            x, right_y = point_r
            p_r += 1

        # max height (i.e. y) between both skylines
        max_y = max(left_y, right_y)

        # if there is a skyline change
        if curr_y != max_y:
            update_output(x, max_y)
            curr_y = max_y

    # there is only left skyline
    append_skyline(p_l, left, n_l, left_y, curr_y)

    # there is only right skyline
    append_skyline(p_r, right, n_r, right_y, curr_y)

    return output

# ----------
# left, right, height
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

buildings = [[0,1,4],[0.5,3,3],[2,4,6],[5,7.5,2],[6,9,4],[6.5,8.5,6]]

# skyline of x and y
print(getSkyline(buildings))


# ----------
# if a building is added.
new_buildings = [[2.5,8,5]]

print(getSkyline(buildings + new_buildings))

