"""
Given an m x n matrix of non-negative integers
representing the height of each unit cell in a
continent, the "Pacific ocean" touches the left
and top edges of the matrix and the "Atlantic
ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down,
left, or right) from a cell to another one with
height equal or lower.

Find the list of grid coordinates where water
can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
(positions with parentheses in above matrix).
"""
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.matrix = matrix
        reaches_pacific = self.get_cluster(
            [(0, n) for n in range(self.n_cols)] + [(n, 0) for n in range(1, self.n_rows)])
        reaches_atlantic = self.get_cluster(
            [(self.n_rows - 1, n) for n in range(self.n_cols)] + [(n, self.n_cols - 1) for n in range(self.n_rows)])
        ans = sorted(list(reaches_pacific & reaches_atlantic))
        return [list(p) for p in ans]

    def get_cluster(self, starting: List[List[int]]) -> set:
        """
        get all the cells from which water can reach one of starting cells
        """
        cur = starting
        reaches = set(starting)
        while cur:
            x, y = cur.pop()
            if x > 0 and (x - 1, y) not in reaches and self.matrix[x - 1][y] >= self.matrix[x][y]:
                cur.append((x - 1, y))
                reaches.add((x - 1, y))
            if x + 1 < self.n_rows and (x + 1, y) not in reaches and self.matrix[x + 1][y] >= self.matrix[x][y]:
                cur.append((x + 1, y))
                reaches.add((x + 1, y))
            if y > 0 and (x, y - 1) not in reaches and self.matrix[x][y - 1] >= self.matrix[x][y]:
                cur.append((x, y - 1))
                reaches.add((x, y - 1))
            if y + 1 < self.n_cols and (x, y + 1) not in reaches and self.matrix[x][y + 1] >= self.matrix[x][y]:
                cur.append((x, y + 1))
                reaches.add((x, y + 1))
        return reaches


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
         [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]]
    ]
    run_tests.run_tests(Solution().pacificAtlantic, correct_answers)