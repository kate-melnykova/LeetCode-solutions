"""
Given two strings word1 and word2, return the minimum number
of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
* Insert a character
* Delete a character
* Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
(*) 0 <= word1.length, word2.length <= 500
(*) word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Runtime complexity: O(len(word1) * len(word2))
        Space complexity: O(len(word1) * len(word2))
        """
        cur = set([(len(word1) - 1, len(word2) - 1), ]) # (symb in word1, symb in word2, changed)
        n_steps = 0
        min_steps = float('inf')
        while cur:
            next_ = set()
            for i1, i2 in cur:
                # get rid of repeating ending
                while i1 >= 0 and i2 >= 0 and word1[i1] == word2[i2]:
                    i1 -= 1
                    i2 -= 1
                # if one of the strings is missing
                if i1 == -1 or i2 == -1:
                    min_steps = min(min_steps, i1 + i2 + 2 + n_steps)
                else:
                    # option1: change the symbol to make them matching
                    next_.add((i1-1, i2-1))
                    # option2: drop a letter from word1
                    next_.add((i1-1, i2))
                    # option3: drop a letter from word2
                    next_.add((i1, i2-1))
            cur = list(next_)
            n_steps += 1
        return min_steps


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        ["horse", "ros", 3],
        ["intention", "execution", 5],
    ]
    print(f"Running tests for minDistance")
    run_tests.run_tests(Solution().minDistance, correct_answers)