"""
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all
i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Example 4:
Input: nums = [100,10,1]
Output: 100


Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = max(nums)
        prev = float('inf')
        cur_sum = 0
        for n in nums:
            if n > 0:
                if prev < n:
                    cur_sum += n
                else:
                    if cur_sum > 0:
                        max_sum = max(max_sum, cur_sum)
                    cur_sum = n
            prev = n
        if cur_sum > 0:
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[10,20,30,5,10,50], 65],
        [[10,20,30,40,50], 150],
        [[12,17,15,13,10,11,12], 33],
        [[100,10,1], 100],
        [[-1, 0, 1], 1],
        [[-3,-2,-1], -1]
    ]
    print(f'Running tests for maxAscendingSum')
    run_tests(Solution().maxAscendingSum, correct_answers)
