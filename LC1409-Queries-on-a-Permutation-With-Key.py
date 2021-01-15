"""
Given the array queries of positive integers between 1 and m,
you have to process all queries[i] (from i=0 to i=queries.length-1)
according to the following rules:

(1) In the beginning, you have the permutation P=[1,2,3,...,m].
(2) For the current i, find the position of queries[i] in the permutation P
(indexing from 0) and then move this at the beginning of the permutation P.
Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.

Example 1:

Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
Explanation: The queries are processed as follow:
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5].
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5].
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5].
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5].
Therefore, the array containing the result is [2,1,2,1].
"""
from typing import List

from run_tests import run_tests


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        rearrange the permuation as needed
        :param queries: query number, 1-indexes
        :param m: total number of queries
        :return: the indexes of requested queries
        """
        self.p = list(range(1, m + 1))
        return [self.do_query(q) for q in queries]

    def do_query(self, q: int) -> int:
        """
        moving query q to the begining of the query.
        :param q: query number, 1-indexed
        :return: the previous index of q
        """
        idx = self.p.index(q)
        self.p.pop(idx)
        self.p = [q, ] + self.p
        return idx


if __name__ == "__main__":
    correct_answers = [
        [[3,1,2,1], 5, [2,1,2,1]],
        [[4,1,2,2], 4, [3,1,2,0]],
        [[7,5,5,8,3], 8, [6,5,0,7,5]]
    ]
    print('Running tests for processQueries')
    run_tests(Solution().processQueries, correct_answers)