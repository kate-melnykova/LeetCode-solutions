"""
Given an integer n, return the decimal value of the binary string formed
by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.

Example 2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.


Constraints:
(*)1 <= n <= 10^5
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        The binary concatenations of 1,2,...,n converted to int modulo 10^9 + 7

        Note that concatenating the binary representations of x and y (bin(x) and bin(y),
        respectively) is equivalent to
        (bin(x) << (len(bin(y))) + bin(y)
        or in decimal representation,
        x * 2^(len(bin(y))) + y.
        Note that modulo operation based on a prime number is a field, i.e., we can split it for
        multiplication and summation. Specifically, for every x and y,
        (x + y) % modulo = x % modulo + y % modulo
        and
        (x * y) % modulo = (x % modulo) * (y % modulo)
        Also,
        (x*y + z) % modulo = ((x % modulo) * y + z) % modulo.

        Then, if the function we want to compute is denoted by f, we need to concatenate
        (concatenation of binaries of 1,2,..., n-1) and binary of n
        f(n) = (f(n-1) * 2^(len(bin(n)) + n ) % 10**9
        This recursion formula may be transfrom to dynamic programming.
        """
        modulo = 10 ** 9 + 7
        if n == 1:
            return 1

        ans = 1
        for m in range(2, n + 1):
            ans = ((ans << (len(str(bin(m))) - 2)) + m) % modulo
        return ans


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [1, 1],
        [3, 27],
        [12, 505379714]
    ]
    print(f'Running tests for concatenatedBinary method')
    run_tests(Solution().concatenatedBinary, correct_answers)