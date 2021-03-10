"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's
added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left
to right. However, the numeral for four is not IIII. Instead,
the number four is written as IV. Because the one is before the
five we subtract it making four. The same principle applies to
the number nine, which is written as IX. There are six instances
where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1 <= num <= 3999
"""


class Solution:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    order = 'IVXLCDM'

    def intToRoman(self, num: int) -> str:
        roman = ''
        i = len(self.order) - 1
        while num:
            roman_tenth, roman_fifth, roman_one = self.order[i], self.order[i - 1], self.order[i - 2]
            n = self.mapping[roman_one]
            roman += roman_tenth * (num // (10 * n))
            num = num % (10 * n)
            if 9 * n <= num:
                roman += roman_one + roman_tenth
                num -= 9 * n
            if 5 * n <= num:
                roman += roman_fifth
                num -= 5 * n
            if 4 * n <= num:
                roman += roman_one + roman_fifth
                num -= 4 * n
            roman += roman_one * (num // n)
            num = num % n
            i -= 2
        return roman


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [3, 'III'],
        [4, 'IV'],
        [9, 'IX'],
        [58, "LVIII"],
        [1994, "MCMXCIV"]
    ]
    print(f'Running tests for intToRoman')
    run_tests(Solution().intToRoman, correct_answers)