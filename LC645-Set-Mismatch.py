"""
You have a set of integers s, which originally contains all the numbers from
1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated
to another number in the set, which results in repetition of one number and loss
of another number.

You are given an integer array nums representing the data status of this set
after the error.

Find the number that occurs twice and the number that is missing and return them
in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
(*) 2 <= nums.length <= 10^4
(*) 1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = None
        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            if nums[n] < 0:
                repeated = n + 1
            else:
                nums[n] = -nums[n]

        for i in range(len(nums)):
            if nums[i] > 0:
                return [repeated, i + 1]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,2,2,4], [2, 3]],
        [[1,1,2,4], [1, 3]],
        [[1,2,3,4,5,3], [3, 6]]
    ]
    print(f'Running tests for findErrorNums')
    run_tests(Solution().findErrorNums, correct_answers)