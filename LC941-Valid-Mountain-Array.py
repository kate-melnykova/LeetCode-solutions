"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

(*) arr.length >= 3
(*) There exists some i with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true


Constraints:
(*) 1 <= arr.length <= 104
(*) 0 <= arr[i] <= 104
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False

        prev = float('-inf')
        state = 'incr'  # mtn is incr, then decr
        for n in arr:
            if n == prev:
                return False

            if prev > n:
                state = 'decr'
            elif state != 'incr':
                return False

            prev = n
        return True


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[2,1], False],
        [[3,5,5], False],
        [[0,3,2,1], True],
        [[1,2,2,1], False]
    ]

    print(f'Running tests for validMountainArray')
    run_tests(Solution().validMountainArray, correct_answers)