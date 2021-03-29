"""
Given a non-empty string containing an out-of-order English
representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its
original digits. That means invalid inputs such as "abc" or
"zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
"""
import collections


class Solution:
    digit_to_word = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    def originalDigits(self, s: str) -> str:
        """
        Runtime complexity: O(n)  # each letter is assessed once, processed at most once
        Space complexity: O(1)  # self.counter stores 10 keys, all dictionaries are of fixed sizes
        """
        self.counter = collections.Counter(s)
        count_digits = [0, ] * 10  # count_digits[i] = total number of digit i in s
        # the following digits have unique letters in their spelling
        unique1 = {
            0: "z",
            2: "w",
            4: "u",
            6: "x",
            8: "g"
        }
        for dig, unique_letter in unique1.items():
            count_digits[dig] = self.counter[unique_letter]
            self.clearDigit(dig, self.counter[unique_letter])

        # now, we are left with 1,3,5,7,9 only
        unique2 = {
            3: "t",
            5: "f",
            7: "s",
        }
        for dig, unique_letter in unique2.items():
            count_digits[dig] = self.counter[unique_letter]
            self.clearDigit(dig, self.counter[unique_letter])

        # now, we are left with 1 and 9 only
        count_digits[1] = self.counter["o"]
        count_digits[9] = self.counter["i"]
        # print(self.counter)
        # print(count_digits)
        all_letters = [dig for dig in range(10) for _ in range(count_digits[dig])]
        return ''.join(map(str, all_letters))

    def clearDigit(self, dig: int, quantity: int) -> None:
        for char in self.digit_to_word[dig]:
            self.counter[char] -= quantity


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        ["owoztneoer", "012"],
        ["fviefuro", "45"],
        ["sevenonefive", "157"],
        ["nien", "9"]
    ]
    print("Running tests for originalDigits")
    run_tests.run_tests(Solution().originalDigits, correct_answers)