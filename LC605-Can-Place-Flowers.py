"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:
(*) 1 <= flowerbed.length <= 2 * 104
(*) flowerbed[i] is 0 or 1.
(*) There are no two adjacent flowers in flowerbed.
(*) 0 <= n <= flowerbed.length
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Running time: O(n)
        Space complexity: O(1)
        """
        max_n_to_be_placed = 0
        prev = 'empty'  # status of prev flowerbed, one of three: empty, reserved, placed
        for place in flowerbed:
            if place == 0 and prev == 'empty':
                max_n_to_be_placed += 1
                prev = 'placed'

            elif place == 0:
                prev = 'empty'
            elif prev == 'placed':
                # note that the current place is reserved
                max_n_to_be_placed -= 1
                prev = 'reserved'
            else:
                # the current place is reserved
                prev = 'reserved'

        return n <= max_n_to_be_placed


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,0,0,0,1], 1, True],
        [[1,0,0,0,1], 2, False],
        [[0,1,0,0,1], 1, False],
        [[0,1,0,1,0,0],1, True],
        [[0,1,0,0,0,1,0,0],2, True]
    ]
    methods = ['canPlaceFlowers', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)