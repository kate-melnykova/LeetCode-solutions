"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:
(*) 1 <= A.length <= 1000
(*) 1 <= A[0].length <= 1000
"""
from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(a) for a in zip(*A)]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]],
        [[[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]]
    ]
    print('Running tests for transpose method')
    run_tests(Solution().transpose, correct_answers)