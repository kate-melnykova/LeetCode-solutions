"""
Find the Most Competitive Subsequence

Given an integer array nums and a positive integer k, return the most competitive
subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero)
elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same
length) if in the first position where a and b differ, subsequence a has a number
less than the corresponding number in b. For example, [1,3,4] is more competitive
than [1,3,5] because the first position they differ is at the final number, and 4
is less than 5.



Example 1:
Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]},
 [2,6] is the most competitive.

Example 2:
Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]


Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            n = nums[i]
            # check if stack[-1] > n and if so, can we afford kicking off stack[-1]
            # we can afford kicking off the last number if the total number of remaining entries
            # (a) in the stack, i.e., len(stack) - 1
            # (b) in nums, i.e., len(nums)-i
            # is at least k
            while stack and stack[-1] > n and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()

            if len(stack) < k:
                stack.append(n)

        return stack


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[3,5,2,6], 2, [2,6]],
        [[2,4,3,3,5,4,9,6], 4, [2,3,3,4]],
        [[0, ]*10000, 5000, [0,]*5000],
        [list(range(100)), 20, list(range(20))],
        [list(range(100, -1, -1)), 20, list(range(19, -1, -1))]
    ]
    methods = ['mostCompetitive', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)
