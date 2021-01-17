"""
Given an integer n, return the number of strings of length n that consist only of vowels
(a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes
before s[i+1] in the alphabet.


Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045


Constraints:
1 <= n <= 50
"""
import itertools

from run_tests import run_tests


class Solution:
    def countVowelStringsDP(self, n: int) -> int:
        """
        Count the number of combinations using dp.

        Observe that if we know the quantity of a, i, o, e, u in a string, then there is a unique
        string that contains such letters in a lexicographical order.
        :param n: the target length of the strings
        :return: number of combos of strings length n made from vowels and in lexicographical order
        Runtime complexity: O(n)
        Space complexity: O(n)
        """
        # if we had just two vowels, then computing the answer is straight-forward
        dp = list(range(1, n + 2))  # dp[i] = number of combos if we had only 2 vowels and length of word is i
        # update dp for 3, 4, and 5 vowels
        # note that all combos of length i may be represented as
        # new vowel at most i times, say j times + any combo of length i - j
        # dp_new[i] = 1 * dp[0] + 1 * dp[1] + ... + 1 * dp[i] = sum(dp[:i+1])
        for _ in range(3):
            dp = list(itertools.accumulate(dp))
        return dp[-1]

    def countVowelStringsSimplified(self, n: int) -> int:
        """
        Number of combos using the math simplification.

        Note that if we had two vowels,
        dp = [1,2,...,n]
        If we had three vowels,
        dp = [1, 1+2, ..., 1 + 2 + ... + n]
        If we had four vowels,
        dp = [1, 2*1+2*1, 3*1 + 2*2 + 1*3, ..., 1*n + 2*(n-1) + ... + n * 1]
        which can be computed quickly.
        Finally, using 5 letters, based on the logic from countVowelStringsDP method, we need to compute the sum
        :param n: target length
        :return: number of combos
        """
        n_combos = 1  # if n == 0
        for i in range(2, n + 2):
            n_combos += sum(a * b for a, b in zip(range(1, i + 1), range(i, 0, -1)))
        return n_combos

    def countVowelStrings(self, n: int) -> int:
        """
        The most mathematical way to compute the total number of combos
        :param n: target length of strings
        :return: number of combos of 'aeiou' of length n that are in lexicographical order
        """
        n += 1
        # simplifying the formula above, we get
        # ans = 1*(1 + 2 + ... + n) + 2*(1 + 2 + ... + (n-1)) + ... + n*(1)
        n_combos = 0  # if n == 1
        # we compute the sum backwards
        sum_first_i = 0
        for i in range(1, n + 1):
            sum_first_i += i
            n_combos += sum_first_i * (n + 1 - i)
        return n_combos


"""
n = 2
2 vowels: dp = [1, 2, 3]
3 vowels: dp = [1, 3, 6]
4 vowels: dp = [1, 4, 10]
5 vowels: dp = [1, 5, 15]
"""

if __name__ == "__main__":
    correct_answers = [
        [1, 5],
        [2, 15],
        [33, 66045]
    ]
    methods = ['countVowelStrings', 'countVowelStringsDP', 'countVowelStringsSimplified']
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)
