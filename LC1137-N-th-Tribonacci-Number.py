"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.


Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537


Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]

        for _ in range(n - 2):
            t.append(sum(t[-3:]))
        return t[-1]


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 4],
        [5, 7],
        [6, 13],
        [25, 1389537]
    ]
    print(f"Testing Tribonacci sequence")
    run_tests.run_tests(Solution().tribonacci, correct_answers)