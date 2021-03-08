"""
Given a string num which represents an integer, return true if num is
a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true


Constraints:
(*) 1 <= num.length <= 50
(*) num consists of only digits.
(*) num does not contain any leading zeros except for zero itself.
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        Runtime complexity: O(n), where n in the number of digits in num, i.e., log(int(num))
        Space complexity: O(1)
        """
        i_start = 0
        i_end = len(num) - 1
        while i_start <= i_end:
            if num[i_start] + num[i_end] not in ['00', '11', '69', '88', '96']:
                return False

            i_start += 1
            i_end -= 1
        return True
if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ['1', True],
        ['2', False],
        ['3', False],
        ['4', False],
        ['5', False],
        ['6', False],
        ['7', False],
        ['8', True],
        ['9', False],
        ['0', True],
        ['11', True],
        ['111', True],
        ['88', True],
        ['89', False],
        ['81', False],
        ['80', False],
        ['69', True],
        ['669', False]
    ]
    print(f'Running tests for isStrobogrammatic')
    run_tests(Solution().isStrobogrammatic, correct_answers)