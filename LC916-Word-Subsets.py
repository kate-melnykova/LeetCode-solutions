"""
We are given two arrays A and B of words.  Each word is a string of
lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in
a, including multiplicity.  For example, "wrr" is a subset of "warrior",
but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.

Example 1:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:
(*) 1 <= A.length, B.length <= 10000
(*) 1 <= A[i].length, B[i].length <= 10
(*) A[i] and B[i] consist only of lowercase letters.
(*) All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from typing import List, Dict
import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        Let m=len(A) and n=len(B).
        Runtime complexity (including calls for self.isSubset): O(m) + O(m*n)= O(mn)
        Space complexity: O(m + n)
        """
        self.criteria: Dict[str, int] = {}
        for b in B:
            for char, freq in collections.Counter(b).items():
                self.criteria[char] = max(self.criteria.get(char, 0), freq)
        return list(filter(self.isSubset, A))

    def isSubset(self, word) -> bool:
        counter = collections.Counter(word)
        return all(counter[char] >= self.criteria[char] for char in self.criteria)


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [["amazon","apple","facebook","google","leetcode"],
         ["e","o"],
         ["facebook","google","leetcode"]],
        [["amazon","apple","facebook","google","leetcode"],
         ["l","e"],
         ["apple","google","leetcode"]],
        [["amazon","apple","facebook","google","leetcode"],
         ["e","oo"],
         ["facebook","google"]],
        [["amazon","apple","facebook","google","leetcode"],
         ["lo","eo"],
         ["google","leetcode"]]
    ]
    print(f'Running tests for wordSubsets')
    run_tests.run_tests(Solution().wordSubsets, correct_answers)