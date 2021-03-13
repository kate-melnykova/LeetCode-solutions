"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.



Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


Constraints:
1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
"""
from typing import List


class Solution:
    def getProducts(self) -> None:
        """
        Runtime complexity: O(n^2)
        Space complexity: O(n)
        """
        # for each element in the arr, say, n we need to find all pairs of numbers whose product is n
        self.products = {}
        self.arr.sort()
        for i, n in enumerate(self.arr):
            i_start = 0
            i_end = i - 1
            while i_start <= i_end:
                prod = self.arr[i_start] * self.arr[i_end]
                if prod == n:
                    self.products[n] = self.products.get(n, []) + [[self.arr[i_start], self.arr[i_end]], ]
                    i_start += 1
                    i_end -= 1
                elif prod > n:
                    i_end -= 1
                else:
                    i_start += 1

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Runtime complexity: O(n^2) (including inside functions)
        Space complexity: O(n^2) (including inside functions)
        """
        self.arr = arr
        self.getProducts()
        self.memo = dict()
        ans = 0
        # we have n possible values of the node of the tree root
        for n in arr:
            ans += self._getNTrees(n)  # get number of trees if root value is n
        return ans


    def _getNTrees(self, rootVal: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if rootVal in self.memo:
            return self.memo[rootVal]

        n_combos = 1  # for single node tree
        for val1, val2 in self.products.get(rootVal, []):
            if val1 == val2:
                n_combos += self._getNTrees(val1) * self._getNTrees(val1)
            else:
                n_combos += 2 * self._getNTrees(val1) * self._getNTrees(val2)
        return n_combos


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [[2,4], 3],
        [[2,4,5,10], 7]
    ]
    print(f'Running tests for numFactoredBinaryTrees')
    run_tests.run_tests(Solution().numFactoredBinaryTrees, correct_answers)