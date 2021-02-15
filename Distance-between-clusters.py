"""
Suppose that matrix mat contains only 'A', 'B', and '0'.
Find the minimum number of steps such that
 (a) you start at any cell whose value is 'A' (you can choose a cell)
 (b) you end at any cell whose value is 'B' (you can choose a cell)
 (c) you can move up, down, left, and right only


Example.
Input.
mat = [
    ['A', '0', '0', '0'],
    ['A', '0', '0', '0'],
    ['0', '0', 'B', 'B']
]
Output: 3
"""
from typing import List

def find_min_steps_non_optimized(mat: List[List[int]]) -> int:
    """
    Find the length of the shortest path between 'A' and 'B'.

    Consider the optimal path. If there are several such paths, choose any.
    There are four options for the starting point 'A' and endpoint 'B':
    (a) 'A' is above or on the same row and to the left of 'B'. Then, the optimal path can be
    represented as moving right first and then, potentially, down
    (b) 'A' is above or on the same row and to the right of 'B'. Then, the optimal path can be
    represented as moving left first and then, potentially, down
    (c) 'A' is below and to the left of 'B'. Then, the optimal path can be
    represented by moving right first, and then up
    (c) 'A' is below and to the right of 'B'. Then, the optimal path can be
    represented by moving left first, and then up.

    All four options share the following: we first move horizontally, and then vertically.
    Checking the optimal option for each case, i.e., for optimal path that moves right and down
    is O(m*n), so the total time complexity is 4*O(mn) = O(mn).
    Space complexity: O(m * n), optimized below.
    """
    min_dist = float('inf')
    n_rows = len(mat)
    n_cols = len(mat[0])
    # if the optimal path from 'A' to 'B' is to the right and down
    min_dist = min(min_dist, _get_distance_from_A(mat, 1, 1))
    # if the optimal path is to the left and down
    min_dist = min(min_dist, _get_distance_from_A(mat, -1, 1))
    # if the optimal paht is to right and up
    min_dist = min(min_dist, _get_distance_from_A(mat, 1, -1))
    # if the optimal path is to the left and up
    min_dist = min(min_dist, _get_distance_from_A(mat, -1, -1))
    return min_dist


def _get_distance_from_A(mat: List[List[int]],
                         i_step: int,
                         j_step: int) -> int:
    """
    return the length of the shortest path 'A' if we allowed to move only as follows:
    if i_step = 1, then downward
    if i_step = -1, then upward
    if j_step = 1, then to the right
    if j_step = -1, then to the left
    For example, if i_step=1 and j_step=-1, we are allowed to move down and left only.
    """
    n_rows = len(mat)
    n_cols = len(mat[0])
    if i_step > 0:
        i_start = 0
        i_end = n_rows  # non-inclusive
    else:
        i_start = n_rows - 1
        i_end = -1  # non-inclusive

    if j_step > 0:
        j_start = 0
        j_end = n_cols  # non-inclusive
    else:
        j_start = n_cols - 1
        j_end = -1  # non-inclusive

    dist_from_A = {i: dict() for i in range(n_rows)}
    # dist_from_A[i][j] is the length of the shortest path from 'A' to mat[i][j]
    # according to the moving rules above

    # note that the path from 'A' to the current point must be in a form (moving to right, then moving down)
    # fill out the first row, i.e., i_start row
    for i in range(i_start, i_end, i_step):
        for j in range(j_start, j_end, j_step):
            if mat[i][j] == 'A':
                # we are at 'A', so the distance to the closest 'A' is zero
                dist_from_A[i][j] = 0
            else:
                # to get from 'A' to the current cell, we need to move either vertically or horizontally
                # if horizontally, then distance would be dist_from_A[i][j-j_step] + 1(if cell exists)
                # if vertically, then the distance would be dist_from_A[i-i_step][j] + 1 (if cell exists)
                dist_from_A[i][j] = min(dist_from_A[i].get(j-j_step, float('inf')),
                                        dist_from_A.get(i-i_step, dict()).get(j, float('inf'))) + 1
                # if there is no previous cell and the current cell is not 'A', assign infinity
    # get the smallest distance to 'B' given dist_from_A
    min_dist = float('inf')
    for i in range(n_rows):
        for j in range(n_cols):
            if mat[i][j] == 'B':
                min_dist = min(min_dist, dist_from_A[i][j])
    return min_dist


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[['A', '0', '0', '0'], ['A', '0', '0', '0'], ['0', '0', 'B', 'B']], 3],
        [[['B', '0', '0'], ['0', '0', 'A']], 3],
        [[['B'], ['A']], 1],
        [[['0', '0', 'B'], ['A', 'A', '0']], 2],
        [[['0', 'B'], ['0', '0'], ['A', '0']], 3]
    ]
    print(f'Running tests for find_min_steps_non_optimized')
    run_tests(find_min_steps_non_optimized, correct_answers)


