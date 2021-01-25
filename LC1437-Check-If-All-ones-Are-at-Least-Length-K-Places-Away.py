""""
Given an array nums of 0s and 1s and an integer k, return True if all 1's
are at least k places away from each other, otherwise return False.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:
Input: nums = [0,1,0,1], k = 1
Output: true


Constraints:
(*) 1 <= nums.length <= 105
(*) 0 <= k <= nums.length
(*) nums[i] is 0 or 1
"""
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        Check that there are at least k empty places between subsequent 1's

        If we see 1, set the cooldown time for k steps
        If we see 0, reduce the cooldown time by 1.
        If we see 1 and cooldown time is still positive, there are less than k empty places between 1's
        :param nums: list, containing 1's and 0's only
        :param k: number of empty places, required
        :return: if the condition can be met

        Runtime complexity: O(n)
        Space complexity: O(1)
        """
        cooldown = -1
        for n in nums:
            if not n:
                cooldown -= 1
            elif cooldown > 0:
                return False

            else:
                cooldown = k
        return True


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,0,0,0,1,0,0,1], 2, True],
        [[1,0,0,1,0,1], 2, False],
        [[1,1,1,1,1], 0, True],
        [[0,1,0,1], 1, True],
        [[0,1,0],1, True],
        [[1,0,0,1,0,0,0,1,0], 2, True],
        [[1, 0, 1, 0, 0, 0, 1, 0], 2, False]
    ]

    methods = ['kLengthApart', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)