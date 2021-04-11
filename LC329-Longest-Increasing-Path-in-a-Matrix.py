"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions:
left, right, up, or down. You may not move diagonally
or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6].
Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1


Constraints:
(*) m == matrix.length
(*) n == matrix[i].length
(*) 1 <= m, n <= 200
(*) 0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List
import bisect

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # sort the entries and store the indexes
        sorted_entries = list()
        for i in range(n_rows):
            for j in range(n_cols):
                bisect.insort(sorted_entries, (matrix[i][j], i, j))

        longest_path = [[1] * n_cols for _ in range(n_rows)]
        max_length = 1
        for val, i, j in sorted_entries:
            length = 0
            if i > 0 and matrix[i - 1][j] < val:
                length = max(length, longest_path[i - 1][j])
            if i + 1 < n_rows and matrix[i + 1][j] < val:
                length = max(length, longest_path[i + 1][j])
            if j > 0 and matrix[i][j - 1] < val:
                length = max(length, longest_path[i][j - 1])
            if j + 1 < n_cols and matrix[i][j + 1] < val:
                length = max(length, longest_path[i][j + 1])

            longest_path[i][j] = length + 1
            max_length = max(max_length, length + 1)
        return max_length


if __name__ == "__main__":
    from run_tests import run_tests

    correct_answers = [
        [[[9,9,4],[6,6,8],[2,1,1]], 4],
        [[[3,4,5],[3,2,6],[2,2,1]], 4],
        [[[1]], 1]
    ]
    print(f"Running tests for longestIncreasingPath")
    run_tests(Solution().longestIncreasingPath, correct_answers)