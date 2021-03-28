"""
Given two strings word1 and word2, return the minimum number of
steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea"
and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:
(*) 1 <= word1.length, word2.length <= 500
(*) word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        We consider all potential substrings word1[i:] and word2[j:]. Therefore,
        Time complexity: O(len(word1) * len(word2))
        Space complexity: O(len(word1) * len(word2))
        """
        self.memo = {}  # key=(word1, word2), value=min number of steps required to get word2 from word1
        return self._minDistance(word1, word2)

    def _minDistance(self, word1: str, word2: str) -> int:
        """
        Worst case.
        Time complexity: O(len(word1) * len(word2))
        Space complexity: O(len(word1) * len(word2))
        """
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        i = 0
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            i += 1

        if i == len(word1) or i == len(word2):
            return abs(len(word2) - len(word1))

        # word1[i] != word2[i]
        # we can drop the ith letter from word1 or from word2
        ans = min(self._minDistance(word1[i+1:], word2[i:]),
                  self._minDistance(word1[i:], word2[i+1:])) + 1
        self.memo[(word1, word2)] = ans
        return ans


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        ["sea", "eat", 2],
        ["leetcode", "etco", 4],
        ["bear", "beer", 2],
        ["identity", "identity", 0],
        ["apple", "applebee", 3],
        ["spy", "officer", 10]
    ]
    print(f'Running tests for minDistance')
    run_tests.run_tests(Solution().minDistance, correct_answers)