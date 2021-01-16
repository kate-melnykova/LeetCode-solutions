"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from typing import List
import bisect

from run_tests import run_tests

class Solution:
    def kth_largest_element_in_an_array(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element in an array
        :param nums: unsorted list of numbers
        :param k: 1 <= k <= n
        :return: the k th largest element in an array

        Time complexity: O(n log k)
        Space complexity: O(k)
        """
        arr = list()
        for n in nums:
            bisect.insort(arr, n)
            if len(arr) > k:
                arr.pop(0)
        return arr[0]


if __name__ == "__main__":
    correct_answers = [
        [[3, 2, 1, 5, 6, 4], 1, 6],
        [[3,2,1,5,6,4], 2, 5],
        [[3,2,3,1,2,4,5,5,6], 4, 4]
    ]
    print('Testing kth_largest_element_in_an_array')
    run_tests(Solution().kth_largest_element_in_an_array, correct_answers)