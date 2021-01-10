""""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        all word representations of digits using the direct iterative approach
        :param digits: digits, from '2' to '9'
        :return: list of all possible word combinations
        """
        if not digits:
            return []

        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combos = set(['', ])
        for digit in digits:
            new_combos = set()
            for encoded in mapping[digit]:
                new_combos = new_combos | set([c + encoded for c in combos])
            combos = set(new_combos)
        return list(combos)


if __name__ == "__main__":
    correct_ans = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"])
    ]
    print('Starting tests for the iterative approach')
    solve = Solution().letterCombinations
    for seq, corr_ans in correct_ans:
        pred_ans = solve(seq)
        pred_ans.sort()
        corr_ans.sort()
        assert pred_ans == corr_ans, f'For input {seq}, got answer {pred_ans}, expected {corr_ans}'
    print('All tests passed')