"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of
those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each
person can be carried by a boat.)
"""
from typing import List
import bisect

from run_tests import run_tests


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        number of boats required to carry people when one boat can fit at most
        2 people and has at most limit weight capacity

        Time complexity: O(n logn) - sorting and n times binary search
        Space complexity: O(1)
        :param people: weights of people
        :param limit: max amount of weight the boat can carry
        :return: number of boats required
        """
        people.sort()
        n_boats = 0
        while people:
            n_boats += 1
            left = limit - people.pop()
            idx = bisect.bisect_left(people, left+1) - 1
            if not people:
                return n_boats
            elif idx >= 0 and people[idx] <= left:
                people.pop(idx)
        return n_boats


if __name__ == '__main__':
    corr_ans = [
        [[1, 2], 3, 1],
        [[3, 2, 2, 1], 3, 3],
        [[3, 5, 3, 4], 5, 4]
    ]
    print(f'Running tests for numRescueBoats method')
    run_tests(Solution().numRescueBoats, corr_ans)