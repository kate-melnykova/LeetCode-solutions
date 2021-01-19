"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
from run_tests import run_tests_belongs


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindrome by increasing the potential length of poly
        :param s:
        :return: the longest palindrome in string s
        Runtime complexity: O(n^2)
        Space complexity: O(n)
        """
        if not s:
            return 0

        # max odd length
        # one letter words
        centers = list(range(len(s)))
        # length of paly 2l + 1
        for l in range(1, len(s) // 2 + 2):
            new_centers = list()
            for center in centers:
                if center + l < len(s) and center - l >= 0 and s[center + l] == s[center - l]:
                    new_centers.append(center)
            if not new_centers:
                break
            else:
                centers = list(new_centers)

        max_odd_length = 2 * l - 1
        max_odd_paly = s[centers[0] - l + 1:centers[0] + l]

        # two letter words
        centers = list()
        for start in range(len(s) - 1):
            if s[start] == s[start + 1]:
                centers.append(start)

        if not centers:
            return max_odd_paly

        # length of paly 2l
        for l in range(2, len(s) // 2 + 2):
            new_centers = list()
            for center in centers:
                if center + l < len(s) and center + 1 - l >= 0 and s[center + l] == s[center + 1 - l]:
                    new_centers.append(center)
            if not new_centers:
                break
            else:
                centers = list(new_centers)
        max_even_length = 2 * l - 2
        max_even_paly = s[centers[0] - l + 2:centers[0] + l]
        if max_even_length > max_odd_length:
            return max_even_paly
        else:
            return max_odd_paly


if __name__ == "__main__":
    correct_answers = [
        ["babad", set(["bab", "aba"])],
        ["ab", set(["a", "b"])],
        ["bb", set(["bb"])],
        ["cbbd", set(["bb"])],
        ["a", set(["a"])],
        ["babadab", set(["badab"])],
        ["babadda", set(["adda"])]
    ]
    methods = ['longestPalindrome']
    for method in methods:
        print(f'Running tests for {method}')
        run_tests_belongs(getattr(Solution(), method), correct_answers)