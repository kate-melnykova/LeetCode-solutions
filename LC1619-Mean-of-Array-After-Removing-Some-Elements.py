"""
Given an integer array arr, return the mean of the remaining
integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10^(-5) of the actual answer will be considered accepted.

Example 1:
Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

Example 2:
Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000

Example 3:
Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
Output: 4.77778

Example 4:
Input: arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
Output: 5.27778

Example 5:
Input: arr = [4,8,4,10,0,7,1,3,7,8,8,3,4,1,6,2,1,1,8,0,9,8,0,3,9,10,3,10,1,10,7,3,2,1,4,9,10,7,6,4,0,8,5,1,2,1,6,2,5,0,7,10,9,10,3,7,10,5,8,5,7,6,7,6,10,9,5,10,5,5,7,2,10,7,7,8,2,0,1,1]
Output: 5.29167


Constraints:
(*) 20 <= arr.length <= 1000
(*) arr.length is a multiple of 20.
(*) 0 <= arr[i] <= 10^5
"""
from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        Runtime complexity: O(n log n)
        Space complexity: O(n)
        """
        # (1) Find 5% of smallest and 5% of largest
        arr.sort()  # O(nlog n), O(1)
        # arr2 = list(sorted(arr)) # O(nlogn), O(n)
        # (2) Remove them
        n = len(arr)  # O(1), O(1)
        five_percent_of_n = int(0.05 * n)  # n // 20 # O(1), O(1)
        arr = arr[five_percent_of_n:-five_percent_of_n]  # O(n), O(0.9 * n)=O(n)
        # (3) Find mean of remaining values
        mean = sum(arr) / len(arr)  # O(n), O(1)
        return mean


"""
def foo(n):
    for i in range(n):
        n = 2 * n
    return n
Upper estimate of space complexity: n cycles * O(1) = O(n)
Actual: only two vars: i and n, memory: O(1)


def foo2(n):
    arr = []
    for i in range(n):
        arr.append(n)
        n = 2 * n
    return arr
Upper estimate: n cycles * O(1) = O(n)
Actual: only three vars: i, n, arr, but arr has length n, O(n)
"""