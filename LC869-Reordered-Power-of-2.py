"""
Starting with a positive integer N, we reorder the digits in any order
(including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting
number is a power of 2.

Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true


Note:

1 <= N <= 10^9
"""
import collections

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # there are very few powers of 2
        # and it must have given number of digits
        n_digits = len(str(N))
        digits_counter = collections.Counter(str(N))
        power = 0
        while power <= 32:
            power_of_two = str(1 << power)
            if len(power_of_two) > n_digits:
                return False

            if len(power_of_two) == n_digits and collections.Counter(power_of_two) == digits_counter:
                return True

            power += 1

        return False


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [1, True],
        [16, True],
        [24, False],
        [46, True],
        [821, True],
        [1420, True],
        [241, False]
    ]
    print(f'Running tests for reorderedPowerOf2')
    run_tests.run_tests(Solution().reorderedPowerOf2, correct_answers)