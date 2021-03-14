"""
You are given two strings s1 and s2 of equal length. A string swap is an
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.


Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Example 4:
Input: s1 = "abcd", s2 = "dcba"
Output: false


Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Runtime complexity: O(n)
        Space complexity: O(1)
        """
        if s1 == s2:
            return True

        swap = []
        swapped = False
        for char1, char2 in zip(s1, s2):
            if char1 != char2 and not swap:
                swap = [char1, char2]

            elif char1 != char2 and not swapped and swap[0] == char2 and swap[1] == char1:
                swapped = True

            elif char1 != char2:
                return False

        return swapped


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["bank", "kanb", True],
        ["kelb", "kelb", True],
        ["abcd", "bcda", False],
        ["abcd", "abce", False],
        ["bbcd", "aacd", False]
    ]
    print(f'Running tests for areAlmostEqual')
    run_tests(Solution().areAlmostEqual, correct_answers)