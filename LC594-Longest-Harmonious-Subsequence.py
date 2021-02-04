"""
We define a harmonious array as an array where the difference between
its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious
subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array
by deleting some or no elements without changing the order of the
remaining elements.


Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

Constraints:
(*) 1 <= nums.length <= 2 * 10^4
(*) -10^9 <= nums[i] <= 10^9
"""
from typing import List
import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        find the longest harmonious (not necessary consecutive) subsequence
        :param nums: list of numbers
        :return: the length of the longest subsequence

        Runtime complexity: O(n)
        Space complexity: O(n)
        """
        c = collections.Counter(nums)
        max_seq = 0
        for n, freq in c.items():
            if c[n + 1] > 0:
                max_seq = max(max_seq, freq + c[n + 1])
        return max_seq


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,3,2,2,5,2,3,7], 5],
        [[1,2,3,4], 2],
        [[1,1,1,1], 0],
        [[1,3,2,2,2,3,7,7,7,7,7,7,7,7,7,7], 5]
    ]
    print('Running tests for find LHS')
    run_tests(Solution().findLHS, correct_answers)