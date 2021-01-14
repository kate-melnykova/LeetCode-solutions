"""
You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array
nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible,
otherwise, return -1.
"""
import bisect
import itertools
from typing import List

from run_tests import run_tests


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Computes the minimum number of operations needed to get sum x.

        Note that the sum of removed numbers is x if the sum of remaining numbers is sum(nums) - x.
        :param nums: non-empty list of positive integers
        :param x: sum to be reached
        :return: minimum number of steps, -1 otherwise
        Time complexity: O(n)
        Space complexity: O(n)
        """
        x = sum(nums) - x # sum of values inside the array
        if not x:
            return len(nums)

        sum_ = 0
        min_steps = float('inf')  # dynamically compute min steps required
        memo = {0: -1}  # key=sum of nums[:i], value=i
        for i, n in enumerate(nums):
            sum_ += n  # total sum from the beginning of the array
            min_steps = min(min_steps, memo.get(sum_ - x, float('inf')) + len(nums) - i)
            memo[sum_] = i # add the value to memo
        return min_steps if min_steps < float('inf') else -1


    def minOperationsNoSpace(self, nums: List[int], x: int) -> int:
        """
        Computes the minimum number of operations needed to get sum x.

        Note that the sum of removed numbers is x if the sum of remaining numbers is sum(nums) - x.
        :param nums: non-empty list of positive integers
        :param x: sum to be reached
        :return: minimum number of steps, -1 otherwise
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        x = sum(nums) - x # sum of values inside the array
        if not x:
            return len(nums)

        nums = list(itertools.accumulate(nums))
        min_steps = float('inf')  # dynamically compute min steps required
        lo = 0
        for i, n in enumerate(nums):
            if n == x:
                # subarray nums[:i] works
                min_steps = min(min_steps, len(nums) - 1 - i)
            else:
                candidate = bisect.bisect_left(nums, n - x, lo=lo, hi=i)
                # check is subarray nums[candidate+1:i] works
                if candidate + 1 < len(nums) and n - nums[candidate] == x:
                    min_steps = min(min_steps, candidate + len(nums) - i)
        return min_steps if min_steps < float('inf') else -1


if __name__ == "__main__":
    corr_answers = [
        [[1,1,4,2,3], 5, 2],
        [[5,6,7,8,9], 4, -1],
        [[3,2,20,1,1,3], 10, 5]
    ]
    print(f'Tests for minOperations started...')
    run_tests(Solution().minOperations, corr_answers)
    print(f'Tests for minOperationsNoSpace started...')
    run_tests(Solution().minOperationsNoSpace, corr_answers)