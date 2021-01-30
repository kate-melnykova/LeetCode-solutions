"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array
any number of times:
(*) If the element is even, divide it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation
    on the last element, and the array will be [1,2,3,(2)].
(*) If the element is odd, multiply it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation
    on the first element, and the array will be [(2),2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3],
then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3


Constraints:
(*) n == nums.length
(*) 2 <= n <= 10^5
(*) 1 <= nums[i] <= 10^9

Hint #1
Assume you start with the minimum possible value for each number so
you can only multiply a number by 2 till it reaches its maximum possible value.
Hint #2
If there is a better solution than the current one, then it must have either its
maximum value less than the current maximum value, or the minimum value larger
than the current minimum value.
Hint #3
Since that we only increase numbers (multiply them by 2), we cannot decrease
the current maximum value, so we must multiply the current minimum number by 2.
"""
from typing import List
import bisect


class Solution:
    def minimumDeviationStartingFromMin(self, nums: List[int]) -> int:
        """
        Following hint 1, the array is modified to start from the smallest values possible

        Runtime complexity: O(nlog n) + O(n log C log n) = O(nlog n log C),
         where n=len(nums) and C is the largest value of C
        (note that integers are not bounded in Python)
        Space complexity: O(n)
        """
        # by doing the operations above, numbers could be changed
        # if all numbers are maxed out, what is the minimum?
        max_of_min_val = min(2 * x if x % 2 else x for x in nums)
        # therefore, if x < max_of_min_val, then it can be doubled.
        # if x = max_of_min_val, then, there is a number is nums, equal to x that couldn't be doubled
        for i in range(len(nums)):
            while not nums[i] % 2:
                nums[i] = nums[i] // 2

        nums.sort()
        min_max_diff = nums[-1] - nums[0]
        while True:
            n = nums.pop(0)  # check if there is a benefit in doubling the smallest element
            if n == max_of_min_val:
                # min could not be doubled, therefore, this is the
                return min_max_diff

            bisect.insort(nums, 2 * n)
            min_max_diff = min(min_max_diff, nums[-1] - nums[0])

    def minimumDeviationStartFromMax(self, nums: List[int]) -> int:
        """
        The array is modified to start from the largest values possible. In this case,
        only one rule is applied: each number can be divided by 2 if even.

        Runtime complexity: O(nlog n) + O(n log C log n) = O(nlog n log C),
         where n=len(nums) and C is the largest value of C
        (note that integers are not bounded in Python)
        Space complexity: O(n)
        """
        # by doing the operations above, numbers could be changed
        # let us figure out max values, and then we can divide them by 2 as long as one can
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] *= 2

        nums.sort()
        min_max_diff = nums[-1] - nums[0]
        while True:
            n = nums.pop()  # check if there is a benefit in doubling the smallest element
            if n % 2:
                # min could not be doubled, therefore, this is the
                return min_max_diff

            bisect.insort(nums, n // 2)
            min_max_diff = min(min_max_diff, nums[-1] - nums[0])


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,2,3,4], 1],
        [[1,4], 0],
        [[4,1,5,20,3], 3],
        [[2,10,8], 3],
        [[17, 19, 31], 7]
    ]
    methods = [
        'minimumDeviationStartFromMax',
        'minimumDeviationStartingFromMin',
    ]
    for method in methods:
        print(f'Run tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)