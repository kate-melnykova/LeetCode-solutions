"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum
equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from typing import List
from collections import Counter

from run_tests import run_tests


class Solution:
    def maxOperations2(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space complexity: O(n)
        """
        pairs = 0
        counter = dict()
        for n in nums:
            if counter.get(k - n, 0):
                pairs += 1
                counter[k - n] -= 1
            else:
                counter[n] = counter.get(n, 0) + 1
        return pairs

    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        The number of disjoint pairs of numbers in nums whose sum equals k
        :param nums:
        :param k:
        :return:
        Time complexity: O(n)
        Space complexity: O(n)
        """
        nums = Counter(nums)
        return sum(min(freq, nums[k - n]) if 2 * n != k else freq for n, freq in nums.items()) // 2


if __name__ == "__main__":
    correct_answers = [
        [[1,2,3,4], 5, 2],
        [[1,2,3,2,4], 5, 2],
        [[3,1,2,3,2,4], 5, 3],
        [[3,1,3,4,3], 6, 1]
    ]
    methods = ['maxOperations', 'maxOperations2', ]
    for method in methods:
        print(f'Starting tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)