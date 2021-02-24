"""
Given a balanced parentheses string S, compute the score of the string based on
the following rule:

(*) "()" has score 1
(*) "AB" has score A + B, where A and B are balanced parentheses strings.
(*) "(A)" has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6


Note:
(*) S is a balanced parentheses string, containing only ( and ).
(*) 2 <= S.length <= 50
"""
from typing import List

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        Time complexity. Each symbol is read once and processed in O(1) manner, so total
        complexity is O(n)
        Space complexity: O(1) without stacking memory, O(max depth) with stacking memory.
        """
        self.S = S

        score = 0
        i = 0
        while i < len(S):
            subscore, i = self._get_score(i)
            score += subscore
        return score

    def _get_score(self, i_start: int) -> List[int]:
        """
        return [score of the balanced string started i_start and ended when the balanced
        string ends (at earliest possible location), first unread char idx]
        """
        if i_start >= len(self.S):
            return [0, len(self.S)]

        score = 0
        i = i_start + 1
        while i < len(self.S) and self.S[i] != ')':
            # nested expression
            sub_score, i = self._get_score(i)
            score += sub_score
        if not score:
            # there were no nested parenthesis expressions:
            return [1, i + 1]

        else:
            return [2 * score, i + 1]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["()", 1],
        ["(())", 2],
        ["()()", 2],
        ["((()))", 4],
        ["(())()", 3],
        ["((())())", 6]
    ]
    print(f'Running tests for scoreOfParentheses')
    run_tests(Solution().scoreOfParentheses,
              correct_answers)