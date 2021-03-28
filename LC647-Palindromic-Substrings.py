"""
Given a string, your task is to count how many palindromic
substrings in this string.

The substrings with different start indexes or end indexes
are counted as different substrings even they consist of
same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.string = s
        ans = 0
        for center in range(len(s)):
            ans += self.countOddPali(center)
        for center in range(len(s) - 1):
            ans += self.countEvenPali(center)
        return ans

    def countOddPali(self, center: int) -> int:
        max_l = 1
        while center - max_l >= 0 and center + max_l < len(self.string) and self.string[center - max_l] == self.string[
            center + max_l]:
            max_l += 1
        return max_l

    def countEvenPali(self, center: int) -> int:
        max_l = 0
        while center - max_l >= 0 and center + 1 + max_l < len(self.string) and self.string[center - max_l] == \
                self.string[center + 1 + max_l]:
            max_l += 1
        return max_l


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        ["abc", 3],
        ["aaa", 6],
        ["abab", 6],
        ["abba", 6],
        ["abbb", 7]
    ]
    print(f"Running tests for countSubstrings")
    run_tests.run_tests(Solution().countSubstrings, correct_answers)