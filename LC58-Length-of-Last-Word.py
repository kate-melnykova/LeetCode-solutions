"""
Given a string s consists of some words separated by spaces,
return the length of the last word in the string. If the last
word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0


Constraints:
(*) 1 <= s.length <= 104
(*) s consists of only English letters and spaces ' '.
"""


class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        word_started = False
        l = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and word_started:
                return l

            elif s[i] != ' ':
                word_started = True
                l += 1

        return l

    def lengthOfLastWord(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        s = s.split()
        return len(s[-1]) if s else 0


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ['', 0],
        [' ', 0],
        ['  ', 0],
        ['word', 4],
        ['Hello World', 5],
        ['Hello Worlds ', 6]
    ]
    methods = ['lengthOfLastWord', 'lengthOfLastWord2', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)