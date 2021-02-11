"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two words are anagrams

        Time complexity: O(n + m), where len(s) = n and len(t) = m
        Space complexity: O(n + m)
        """
        return sorted(s) == sorted(t)

    def is_anagram(self, s: str, t: str) -> bool:
        """
        Check if strings s and t are anagrams

        Time complexity: O(n + m)
        Space complexity: O(n + m)
        """
        if len(s) != len(t):
            return False

        counter = dict()
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            if counter.get(char, 0) < 1:
                return False

            counter[char] -= 1
        return True


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ['abc', 'cab', True],
        ['abcd', '', False],
        ['abc', 'abd', False],
        ['qweryt', 'ytrewq', True],
        ['12;', ';12', True],
        ['', '', True],
        ['avaa', 'aava', True],
        ['avaa', 'avva', False],
        ['.,;', ';.,', True],
        ['.,;', '..,', False]
    ]
    methods = ['isAnagram', 'is_anagram']
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)