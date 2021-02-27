"""
 Given two integers dividend and divisor, divide two integers without
 using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing
 its fractional part. For example, truncate(8.345) = 8 and
 truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For this problem,
assume that your function returns 231 − 1 when the division result overflows.


Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1


Constraints:
(*) -2^31 <= dividend, divisor <= 2^31 - 1
(*) divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        # determine the sign:
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor

        int_part = 0
        powers = (1, divisor)  # one of [(1, divisor), (2, divisor *2), (4, divisor * 4),...]
        # get the largest power of interest out powers
        while powers[1] < dividend:
            powers = (powers[0] << 1, powers[1] << 1)

        while powers[0] > 0:
            if dividend >= powers[1]:
                int_part += powers[0]
                dividend -= powers[1]
            powers = (powers[0] >> 1, powers[1] >> 1)

        if sign < 0:
            int_part = -int_part

        return min(int_part, (1 << 31) - 1)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [10, 3, 3],
        [-10, 3, -3],
        [10, -3, -3],
        [-10, -3, 3],
        [-(1<<31), -1, (1<<31) - 1],
        [-7, -2, 3]
    ]
    print('Running tests for divide method')
    run_tests(Solution().divide, correct_answers)