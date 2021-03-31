"""
You are given a 2D array of integers envelopes where
envelopes[i] = [wi, hi] represents the width and the
height of an envelope.

One envelope can fit into another if and only if both
the width and height of one envelope are greater than
the other envelope's width and height.

Return the maximum number of envelopes you can Russian
doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can
Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1


Constraints:
1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""
from typing import List
import itertools
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        n = len(envelopes)
        Runtime complexity: O(n log n)
        Space complexity: O(n)
        """
        widths = list(sorted(set(e[0] for e in envelopes)))
        heights = {h: i for i, h in enumerate(sorted(set(e[1] for e in envelopes)))}
        envelopes_dct = dict()
        for w, h in envelopes:
            if w not in envelopes_dct:
                envelopes_dct[w] = list()
            bisect.insort(envelopes_dct[w], h)

        enclosed = [0] * len(heights)
        for w in widths:
            for h in reversed(envelopes_dct[w]):
                i = heights[h]
                if i > 0:
                    enclosed[i] = enclosed[i - 1] + 1
                else:
                    enclosed[i] = 1
            enclosed = list(itertools.accumulate(enclosed, max))
        return enclosed[-1]


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [[[5,4],[6,4],[6,7],[2,3]], 3],
        [[[1,1],[1,1],[1,1]], 1]
    ]
    print(f"Running tests for maxEnvelopes")
    run_tests.run_tests(Solution().maxEnvelopes, correct_answers)
