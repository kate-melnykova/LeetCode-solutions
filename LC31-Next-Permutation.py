"""
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the
lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]


Constraints:
(*) 1 <= nums.length <= 100
(*) 0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        # pre-plan
        # if nums[-2] < nums[-1], swap them, and we are done
        # elif nums[-3] < nums[-2], then select the smallest element in nums[-2:]
        # which is larger than nums[-3], swap it with nums[-3] and sort the remaining array.
        # Note that the array is almost sorted in opposite order already (except the
        # swapped element)

        # note the largest element of nums[]
        # going through nums from right to left
        # i -> len(nums) - 1 to 1
        # find the first instance when nums[i-1] < nums[i]
        i = len(nums) - 1
        idx_found = False
        while i > 0 and not idx_found:
            if nums[i - 1] < nums[i]:
                idx_found = True
            else:
                i -= 1

        if idx_found:
            # find the smallest element in nums[i:] which is larger than nums[i-1]
            n = nums[i - 1]
            min_larger_than_n = nums[i]
            min_larger_than_n_idx = i
            for j in range(i + 1, len(nums)):
                if n < nums[j] <= min_larger_than_n:
                    min_larger_than_n = nums[j]
                    min_larger_than_n_idx = j
            # swap these numbers
            nums[i - 1], nums[min_larger_than_n_idx] = nums[min_larger_than_n_idx], nums[i - 1]
        else:
            # we are at the largest seq possible
            # to get the smallest possible, reverse it
            i = 0

        # revert the nums[i:]. Note that it is reversed-sorted except, potentially,
        # swapped number
        # but we swapped number is the smallest number in nums[i:] larger than some
        # threshold, so the array is still sorted
        i_start = i
        i_end = len(nums) - 1
        while i_start <= i_end:
            # recall that we know that nums[i_start] >= nums[i_end] except when j is i_start or i_end
            nums[i_start], nums[i_end] = nums[i_end], nums[i_start]
            i_start += 1
            i_end -= 1


if __name__ == "__main__":
    from run_tests import run_tests

    correct_answers = [
        [[1,2,3], [1,3,2]],
        [[3,2,1], [1,2,3]],
        [[1,1,5], [1,5,1]],
        [[1,2,2], [2,1,2]],
        [[1], [1]],
        [[1,2,3,1], [1,3,1,2]],
        [[1,2,4,3,4], [1,2,4,4,3]]
    ]
    print(f'Run tests for nextPermutation')

    def to_test(arr):
        Solution().nextPermutation(arr)
        return arr

    run_tests(to_test, correct_answers)