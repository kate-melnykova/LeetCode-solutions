"""
Given an integer array nums, you need to find one continuous subarray
that if you only sort this subarray in ascending order, then the whole
array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0


Constraints:
(*) 1 <= nums.length <= 10^4
(*) -10^5 <= nums[i] <= 10^5
"""
import bisect
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Time complexity: the array is passed twice (once from left to right, once
        right to left). Two bisects require at most O(log n) each, so total time
        complexity is O(n)

        Space complexity: O(1)
        """
        incr_seq_idx = 1
        while incr_seq_idx < len(nums) and nums[incr_seq_idx - 1] <= nums[incr_seq_idx]:
            incr_seq_idx += 1

        if incr_seq_idx == len(nums):
            # the array is sorted
            return 0

        min_after_seq = min(nums[i] for i in range(incr_seq_idx, len(nums)))
        i_start_to_sort = bisect.bisect_left(nums, min_after_seq + 1, hi=incr_seq_idx)

        decr_seq_idx = len(nums) - 1
        while decr_seq_idx and nums[decr_seq_idx - 1] <= nums[decr_seq_idx]:
            decr_seq_idx -= 1

        max_before_seq = max(nums[i] for i in range(decr_seq_idx))
        i_end_to_sort = bisect.bisect_left(nums, max_before_seq, lo=decr_seq_idx)
        return i_end_to_sort - i_start_to_sort


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[2,6,4,8,10,9,15], 5],
        [[1,2,3,4], 0],
        [[1], 0],
        [[1,3,2], 2],
        [[1,2,3,2], 2],
        [[2,1,2,3], 2]
    ]
    print(f'Running tests for findUnsortedSubarray')
    run_tests(Solution().findUnsortedSubarray, correct_answers)