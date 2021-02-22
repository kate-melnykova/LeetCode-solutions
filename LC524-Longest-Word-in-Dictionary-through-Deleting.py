"""
Given a string and a string dictionary, find the longest string in the dictionary
that can be formed by deleting some characters of the given string. If there are
more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output:
"a"
Note:
(*) All the strings in the input will only contain lower-case letters.
(*) The size of the dictionary won't exceed 1,000.
(*) The length of all the strings in the input won't exceed 1,000.
"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        """
        Time complexity: O((n+m) len(d)), where n is the length of s, m is the average length of words in d
        Space complexity: O(1)
        """
        self.s = s
        longest_string = ''
        for substring in d:
            if (len(substring) > len(longest_string) or (
                    len(substring) == len(longest_string) and substring < longest_string)) and self.isSubString(
                    substring):
                longest_string = substring
        return longest_string

    def isSubString(self, substring: str) -> bool:
        """
        Time complexity: O(len(s) + len(substring))
        Space complexity: O(1)
        """
        i = 0
        for char in self.s:
            if i == len(substring):
                return True

            if char == substring[i]:
                i += 1
        return i == len(substring)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["abpcplea", ["ale","apple","monkey","plea"], "apple"],
        ["abpcplea", ["a","b","c"], "a"]
    ]
    print(f'Running tests for findLongestWord')
    run_tests(Solution().findLongestWord, correct_answers)