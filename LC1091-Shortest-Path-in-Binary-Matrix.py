"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.
If such a path does not exist, return -1.

Example 1:
Input: [[0,1],[1,0]]
Output: 2

Example 2:
Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Note:
(*) 1 <= grid.length == grid[0].length <= 100
(*) grid[r][c] is 0 or 1
"""
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        cur = [(0, 0), ]
        visited = set(cur)
        n_steps = 1
        while cur:
            next_ = list()
            for i, j in cur:
                if i == n - 1 and j == n - 1:
                    return n_steps
                # left
                if i > 0 and (i - 1, j) not in visited and not grid[i - 1][j]:
                    next_.append((i - 1, j))
                    visited.add((i - 1, j))
                # upper-left
                if i > 0 and j > 0 and (i - 1, j - 1) not in visited and not grid[i - 1][j - 1]:
                    next_.append((i - 1, j - 1))
                    visited.add((i - 1, j - 1))
                # lower-left
                if i > 0 and j + 1 < n and (i - 1, j + 1) not in visited and not grid[i - 1][j + 1]:
                    next_.append((i - 1, j + 1))
                    visited.add((i - 1, j + 1))
                # up
                if j > 0 and (i, j - 1) not in visited and not grid[i][j - 1]:
                    next_.append((i, j - 1))
                    visited.add((i, j - 1))
                # down
                if j + 1 < n and (i, j + 1) not in visited and not grid[i][j + 1]:
                    next_.append((i, j + 1))
                    visited.add((i, j + 1))
                # right
                if i + 1 < n and (i + 1, j) not in visited and not grid[i + 1][j]:
                    next_.append((i + 1, j))
                    visited.add((i + 1, j))
                # upper-right
                if i + 1 < n and j > 0 and (i + 1, j - 1) not in visited and not grid[i + 1][j - 1]:
                    next_.append((i + 1, j - 1))
                    visited.add((i + 1, j - 1))
                # lower-right
                if i + 1 < n and j + 1 < n and (i + 1, j + 1) not in visited and not grid[i + 1][j + 1]:
                    next_.append((i + 1, j + 1))
                    visited.add((i + 1, j + 1))
            cur = list(next_)
            n_steps += 1
        return -1


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
       [[[0,1],[1,0]], 2],
       [[[0,0,0],[1,1,0],[1,1,0]], 4]
    ]
    run_tests(Solution().shortestPathBinaryMatrix, correct_answers)
    print('All tests completed')