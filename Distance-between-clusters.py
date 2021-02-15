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

"""
####
Approach 1: BFS
Assume that we start at all cells 'A' and use the BFS to reach cells 'B'
####
"""
def find_min_steps_bfs(mat: List[List[int]]) -> int:
    """
    Runtime complexity: O(mn)
    Space complexity: O(mn)
    """
    n_rows = len(mat)
    n_cols = len(mat[0])
    visited = set()
    cur = list()
    #get initial positions of 'A'
    for i in range(n_rows):
        for j in range(n_cols):
            if mat[i][j] == 'A':
                visited.add((i, j))
                cur.append((i, j))
    # bfs
    n_steps = 0
    while cur:
        next_ = list()
        for i, j in cur:
            if mat[i][j] == 'B':
                return n_steps

            # up
            if i > 0 and (i-1, j) not in visited:
                next_.append((i-1, j))
                visited.add((i-1, j))
            # down
            if i + 1 < n_rows and (i+1, j) not in visited:
                next_.append((i+1, j))
                visited.add((i+1, j))
            # left
            if j > 0 and (i, j-1) not in visited:
                next_.append((i, j-1))
                visited.add((i, j-1))
            # right
            if j + 1 < n_cols and (i, j+1) not in visited:
                next_.append((i, j+1))
                visited.add((i, j+1))
        cur = list(next_)
        n_steps += 1
    return float('inf')


"""
####
Approach 2. Dynamic programming
Build a matrix with distances to the closest 'A'.
This approach is not optimized
####
"""

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
    Space complexity: O(m * n), optimized in the next approach.
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


"""
####
Approach 3. Dynamic programming
In the approach above, we can:
(a) compute min_dist when compute dist_from_A
(b) not store the whole matrix -- we need access only to the last row
####
"""
def find_min_steps_dp_optimized(mat: List[List[int]]) -> int:
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
    Space complexity: O(n)
    """
    min_dist = float('inf')
    n_rows = len(mat)
    n_cols = len(mat[0])
    # if the optimal path from 'A' to 'B' is to the right and down
    min_dist = min(min_dist, _get_distance_from_A_optimized(mat, 1, 1))
    # if the optimal path is to the left and down
    min_dist = min(min_dist, _get_distance_from_A_optimized(mat, -1, 1))
    # if the optimal paht is to right and up
    min_dist = min(min_dist, _get_distance_from_A_optimized(mat, 1, -1))
    # if the optimal path is to the left and up
    min_dist = min(min_dist, _get_distance_from_A_optimized(mat, -1, -1))
    return min_dist


def _get_distance_from_A_optimized(mat: List[List[int]],
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

    min_dist = float('inf')
    dist_from_A = {i: float('inf') for i in range(-1, n_cols+1)}
    # dist_from_A[i][j] is the length of the shortest path from 'A' to mat[i][j]
    # according to the moving rules above

    # note that the path from 'A' to the current point must be in a form (moving to right, then moving down)
    # fill out the first row, i.e., i_start row
    for i in range(i_start, i_end, i_step):
        for j in range(j_start, j_end, j_step):
            if mat[i][j] == 'A':
                # we are at 'A', so the distance to the closest 'A' is zero
                dist_from_A[j] = 0
            else:
                # to get from 'A' to the current cell, we need to move either vertically or horizontally
                # if horizontally, then distance would be dist_from_A[i][j-j_step] + 1(if cell exists)
                # if vertically, then the distance would be dist_from_A[i-i_step][j] + 1 (if cell exists)
                dist_from_A[j] = min(dist_from_A[j-j_step], dist_from_A[j]) + 1
                # if there is no previous cell and the current cell is not 'A', assign infinity
            if mat[i][j] == 'B':
                min_dist = min(min_dist, dist_from_A[j])
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
    print(f'Running tests for find_min_steps_bfs')
    run_tests(find_min_steps_bfs, correct_answers)
    print(f'Running tests for find_min_steps_non_optimized')
    run_tests(find_min_steps_non_optimized, correct_answers)
    print(f'Running tests for find_min_steps_dp_optimized')
    run_tests(find_min_steps_dp_optimized, correct_answers)


