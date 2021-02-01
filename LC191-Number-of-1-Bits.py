"""
Write a function that takes an unsigned integer and returns the number of
'1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type.
In this case, the input will be given as a signed integer type. It should not
affect your implementation, as the integer's internal binary representation is
the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above, the input represents the signed integer. -3.
Follow up: If this function is called many times, how would you optimize it?



Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of
three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of
one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total
of thirty one '1' bits.


Constraints:
(*) The input must be a binary string of length 32
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Convert to binary and add digits
        Time and space complexity: O(1) (both)
        """
        return sum(map(int, f'{n:032b}'))

    def hammingWeight2(self, n: int) -> int:
        """
        Convert to binary and count number of ones
        Time and space complexity: O(1) (both)
        """
        return bin(n).count('1')

    def hammingWeightBinary(self, n: int) -> int:
        """
        If n is not zero, exclude the least significant digit
        and add it to ans
        Time and space complexity: O(1) (both)
        """
        one_bytes = 0
        while n:
            one_bytes += 1
            n = n & (n-1)
        return one_bytes


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [11, 3],
        [1, 1],
        [8, 1],
        [1024, 1],
        [(1 << 31) - 1, 31]
    ]
    methods = ['hammingWeight', 'hammingWeight2', 'hammingWeightBinary']
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)