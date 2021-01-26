"""
You may recall that an array arr is a mountain array if and only if:

(*) arr.length >= 3
(*) There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums, return the minimum number of elements to remove
to make nums a mountain array.

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5,
 making the array nums = [1,5,6,3,1].

Example 3:
Input: nums = [4,3,2,1,1,2,3,1]
Output: 4

Example 4:
Input: nums = [1,2,3,4,4,3,2,1]
Output: 1


Constraints:
(*) 3 <= nums.length <= 1000
(*) 1 <= nums[i] <= 109
(*) It is guaranteed that you can make a mountain array out of nums.
"""
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space: O(n)
        """
        # find the max number of elements to keep
        dp_mtn = []  # list of tuples (the last number in mtn, length of mtn)
        dp_incr = [(float('-inf'), 0), ]  # list of tuples (the last number in incr seq, length of incr seq)
        """
        nums = [1, 3, 1]
        n = 1  arr = [1]
          dp_mtn = []
          dp_incr = [(float('-inf'), 0), (1, 1)]
        n = 3 arr = [1, 3]
          dp_mtn = []
          dp_incr = [(float('-inf'), 0), (1, 1), (3, 2)]
        n = 1 arr = [1,3,1]
          dp_mtn = [(1, 3), ]
          dp_incr = [(float('-inf'), 0), (1, 1), (1, 1), (3, 2)]
          candidates for mtn: (3, 2) -> with n=1, the length of seq is 3

        if dp_mtn is empty:
          return None
        else:
          return len(nums) - the longest montain max(dp_mtn's 2nd number in the tuple)
        """
        for n in nums:
            # add to dp_incr
            max_incr_seq = 0
            for last_number, l in dp_incr:
                if last_number < n:
                    max_incr_seq = max(max_incr_seq, l + 1)
            dp_incr.append((n, max_incr_seq))

            # add the seq that ends on n to dp_mtn
            max_mtn = 0
            # (a) extend existing mtn
            for last_number, l in dp_mtn:
                if last_number > n:
                    max_mtn = max(max_mtn, l + 1)
            # (b) converting increasing seq to mtn
            for last_number, l in dp_incr:
                if last_number > n:
                    max_mtn = max(max_mtn, l + 1)
            if max_mtn >= 3:
                dp_mtn.append((n, max_mtn))

        if not dp_mtn:
            return None
        else:
            return len(nums) - max(dp_mtn, key=lambda x: x[1])[1]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,3,1], 0],
        [[2,1,1,5,6,2,3,1], 3],
        [[4,3,2,1,1,2,3,1], 4],
        [[1,2,3,4,4,3,2,1], 1]
    ]

    print(f'Runnging tests for minimumMountainRemovals')
    run_tests(Solution().minimumMountainRemovals, correct_answers)