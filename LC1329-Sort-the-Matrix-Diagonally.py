"""
A matrix diagonal is a diagonal line of cells starting from some cell in either
the topmost row or leftmost column and going in the bottom-right direction until
reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0],
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order
and return the resulting matrix.

Example 1.
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Constraints:
(1) m == mat.length
(2) n == mat[i].length
(3) 1 <= m, n <= 100
(4) 1 <= mat[i][j] <= 100
"""
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(mat), len(mat[0]) # 3, 4
        for diag in range(n_cols):
            line = [mat[i][i+diag] for i in range(min(n_rows, n_cols-diag))]
            line.sort()
            for i, n in enumerate(line):
                mat[i][i+diag] = n
        for diag in range(1, n_rows):
            line = [mat[j+diag][j] for j in range(min(n_cols, n_rows-diag))]
            line.sort()
            for j, n in enumerate(line):
                mat[j+diag][j] = n
        return mat


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]]],
        [[[1, 2]], [[1, 2]]],
        [[[1], [2]], [[1], [2]]],
        [[[2,2], [1, 1]], [[1, 2], [1, 2]]],
        [[[2,3,4], [1,0,1]], [[0, 1, 4], [1,2,3]]]
    ]
    methods = ['diagonalSort', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)