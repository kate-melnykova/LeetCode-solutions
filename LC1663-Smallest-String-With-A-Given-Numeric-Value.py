"""
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as
the sum of its characters' numeric values. For example, the numeric value of
the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest
string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes
before y in dictionary order, that is, either x is a prefix of y, or if i is
the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27,
and it is the smallest string with such a value and length equal to 3.

Example 2:
Input: n = 5, k = 73
Output: "aaszz"


Constraints:
(*) 1 <= n <= 10^5
(*) n <= k <= 26 * n
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # recursive solution
        # assign the first letter to be the smallest possible:
        # (1) check if 'a' is the first letter, can we make the word (with additional 'room')
        # to do this, check if the sum of 'azzz...z' is more than k
        # mathematically, check if 1 + 26*(n-1) = 26n - 25 > k
        # (2) if so, assign 'a' and enter the recursion mode f(n-1, k-1)
        # (3) if not, assign the smallest letter possible, i.e, the string will be
        # '?zzz...z' whose sum is code(?) + 26*(n-1) = k, so code(?) = k - 26 * (n-1)
        """
        # recursive solution
        if n == 1:
            return chr(ord('a') + (k-1))

        elif 26 * n - 25 > k:
            return 'a' + self.getSmallestString(n-1, k-1)

        else:
            shift = k - 26*(n-1) - 1
            #print(shift)
            return chr(ord('a') + (k-1) - 26 * (n-1)) + 'z' * (n-1)
        """
        # dp solution
        ans = ''
        while n:
            if 26 * n - 25 > k:
                ans += 'a'
                n -= 1
                k -= 1
            else:
                ans += chr(ord('a') + (k - 1) - 26 * (n - 1)) + 'z' * (n - 1)
                n = 0
        return ans


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [2, 4, 'ac'],
        [3, 3, 'aaa'],
        [3, 27, 'aay'],
        [5, 73, 'aaszz'],
        [2, 52, 'zz']
    ]

    print(f'Running tests for getSmallestString')
    run_tests(Solution().getSmallestString, correct_answers)