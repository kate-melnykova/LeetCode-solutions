"""
Given a string s consisting only of letters 'a' and 'b'. In a single step you can
remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some
characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.


Example 1:
Input: s = "ababa"
Output: 1
Explanation: String is already palindrome

Example 2:
Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "".
Remove palindromic subsequence "a" then "bb".

Example 3:
Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "".
Remove palindromic subsequence "baab" then "b".
Example 4:

Input: s = ""
Output: 0


Constraints:
0 <= s.length <= 1000
s only consists of letters 'a' and 'b'
"""


class Solution:
    def removePalindromeSubConsecutive(self, s: str) -> int:
        """
        The question needs interpretation: if the subsequence has to
        contain consecutive letters. This function solves it for
        consecutive case

        Time complexity: we need to consider each potential substring once.
        There are O(n^2) substrings and each of them requires O(n) time to
        check for the number of steps. In total: O(n^2)

        Space complexity: O(n^2) for the dictionary.
        """
        if not s:
            return 0

        self.memo = {'a': 1, 'b': 1, 'ab': 2, 'ba': 2}  # key = string, value = n steps
        self._removePalindromeSub(s)
        return self.memo[s]

    def _removePalindromeSub(self, s: str) -> int:
        """
        For consecutive substrings
        """
        if s in self.memo:
            return self.memo[s]

        # check if the string is a palindrome
        if self.isPalindrome(s):
            self.memo[s] = 1
            return 1

        # note that if the length of the string is 1 or 2, one of the if cases above holds

        min_steps = len(s)  # if we remove letter by letter, this is the required number of steps
        # consider the last removal of palindrome
        # it always may be chosen in a way that it contains the last letter of s
        # there are two cases: the original first letter of s belong to that final palindrome or not
        # if it belongs, then we can exclude these letters
        if s[0] == s[-1]:
            min_steps = min(min_steps, self._removePalindromeSub(s[1:-1]))
        # if the first letter does not belong to the final palindrome (containing the last letter),
        # then the string s can be split into two and do operations separately
        for i in range(1, len(s)):
            steps_left = self._removePalindromeSub(s[:i])
            steps_right = self._removePalindromeSub(s[i:])
            min_steps = min(min_steps, steps_left + steps_right)
        self.memo[s] = min_steps
        return min_steps

    def removePalindromeSubNonConsecutive(self, s: str) -> int:
        """
        The number of palindrome removal if subsequence is not necessary consecutive.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not s:
            return 0

        elif self.isPalindrome(s):
            return 1

        else:
            # remove all 'a' first, then remove all 'b'
            return 2

    def isPalindrome(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i_start = 0
        i_end = len(s) - 1
        while i_start < i_end and s[i_start] == s[i_end]:
            i_start += 1
            i_end -= 1
        return s[i_start] == s[i_end]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers_conseq = [
        ['a', 1],
        ['aa', 1],
        ['aba', 1],
        ['abab', 2],
        ['bbaabbaabbbbbaa', 2],
        ['baaaabb', 2],
        ['ababbabbb', 3],
        ['', 0]
    ]
    print(f'Running tests for removePalindromeSubConsecutive')
    run_tests(Solution().removePalindromeSubConsecutive, correct_answers_conseq)

    correct_answers_nonconseq = [
        ['a', 1],
        ['aa', 1],
        ['aba', 1],
        ['abab', 2],
        ['bbaabbaabbbbbaa', 2],
        ['baaaabb', 2],
        ['ababbabbb', 2],
        ['', 0],
        ['ababa', 1]
    ]
    print(f'Running tests for removePalindromeSubNonConsecutive')
    run_tests(Solution().removePalindromeSubNonConsecutive, correct_answers_nonconseq)