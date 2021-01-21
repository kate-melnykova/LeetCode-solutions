"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
(1) Open brackets must be closed by the same type of brackets.
(2) Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true


Constraints:
(1) 1 <= s.length <= 104
(2) s consists of parentheses only '()[]{}'.
"""
from run_tests import run_tests

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validating that string s is valid using stack approach
        :param s: string containing '(){}[]' only
        :return: brackets are balanced
        Runtime complexity: O(n)
        Space complexity: O(n) worstcase
        """
        open_brackets = []  # stack of open but not closed brackets
        for char in s:
            if char in ['(', '[', '{']:
                open_brackets.append(char)
            else:
                try:
                    complement = open_brackets.pop()
                except IndexError:
                    return False
                else:
                    if complement + char not in ['()', '[]', '{}']:
                        return False
        return not len(open_brackets)


if __name__ == "__main__":
    correct_answers = [
        ['()', True],
        ['()[]{}', True],
        ['(', False],
        [')', False],
        ['())', False],
        ['({})', True],
        ['[][]', True],
        ['(]', False],
        ['([)]', False]
    ]
    methods = ['isValid', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)