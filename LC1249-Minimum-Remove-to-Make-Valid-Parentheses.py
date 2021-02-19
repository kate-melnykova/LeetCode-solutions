"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:
(*) 1 <= s.length <= 10^5
(*) s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_keep = list()
        bal = 0
        for char in s:
            if char == '(':
                to_keep.append('(')
                bal += 1
            elif char == ')' and bal:
                to_keep.append(')')
                bal -= 1
            elif char != ')':
                to_keep.append(char)
        # balance is non-negative, but we need to make it zero
        to_keep2 = list()
        bal2 = 0
        for char in reversed(to_keep):
            if char == ')':
                to_keep2.append(')')
                bal2 -= 1
            elif char == '(' and bal2 < 0:
                to_keep2.append('(')
                bal2 += 1
            elif char != '(':
                to_keep2.append(char)
        return ''.join(reversed(to_keep2))


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["lee(t(c)o)de)", "lee(t(c)o)de"],
        ["a)b(c)d", "ab(c)d"],
        ["))((", ""],
        ["(a(b(c)d)", "a(b(c)d)"]
    ]
    print(f"Running tests for minRemoveToMakeValid")
    run_tests(Solution().minRemoveToMakeValid, correct_answers)