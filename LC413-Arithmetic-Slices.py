"""
A sequence of numbers is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
The following sequence is not arithmetic.
    1, 1, 2, 5, 7
A zero-indexed array A consisting of N numbers is given. A slice of that array
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:
A = [1, 2, 3, 4]
return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if len(A) < 3:
            return 0

        n_seq = 0
        diff = A[1] - A[0]
        cur_seq = 2
        prev = A[1]
        for i in range(2, len(A)):
            a = A[i]
            if a - prev == diff:
                cur_seq += 1
                n_seq += cur_seq - 2
            else:
                cur_seq = 2
                diff = a - prev
            prev = a
        return n_seq


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,2,3,4], 3],
        [[1,2,3,4,5], 6],
        [[1,2,3,4,5,7], 6],
        [[1, -1, -3], 1],
        [[1,-1,-3,-1,1], 2]
    ]
    print(f'Running tests for numberOfArithmeticSlices')
    run_tests(Solution().numberOfArithmeticSlices, correct_answers)