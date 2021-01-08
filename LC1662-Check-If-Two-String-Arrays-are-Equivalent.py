""""
Given two string arrays word1 and word2, return true if the two arrays represent
the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order
forms the string.
"""
from typing import List


class Solution:

    def arrayStringsAreEqualDirect(self, word1: List[str], word2: List[str]) -> bool:
        """
        direct approach for checking if the list of strings are equivalent
        :param word1: list of strings that form the first word
        :param word2: list of strings that form the second word
        :return: if concatenating word1 and word2 yield identical result
        """
        return ''.join(word1) == ''.join(word2)

    def arrayStringsAreEqualNoSpace(self, word1: List[str], word2: List[str]) -> bool:
        """
        comparing if concatenation of strings in word1 and word2 yield identical results
        assuming that available memory is O(1)
        """
        i1 = 0  # index of word1
        i2 = 0  # index of word1[i1]
        j1 = 0  # index of word2
        j2 = 0  # index of word2[j1]
        while i1 < len(word1) and j1 < len(word2):
            # we want to compare word1[i1][i2] and word2[j1][j2]
            if len(word1[i1]) == i2:
                i1 += 1
                i2 = 0
            elif len(word2[j1]) == j2:
                j1 += 1
                j2 = 0
            elif word1[i1][i2] == word2[j1][j2]:
                i2 += 1
                j2 += 1
            else:
                return False

        return i1 == len(word1) and j1 == len(word2) - 1 and j2 == len(word2[-1])

if __name__ == '__main__':
    s = Solution()
    correct_ans = (
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True)
    )
    print('Testing arrayStringsAreEqualDirect...')
    for word1, word2, corr_ans in correct_ans:
        pred_ans = s.arrayStringsAreEqualDirect(word1, word2)
        assert(pred_ans == corr_ans), f"For {word1} and {word2}, got answer {pred_ans}, expected {corr_ans}"

    print('All tests for arrayStringsAreEqualDirect passed')
    print('Testing arrayStringsAreEqualNoSpace...')
    for word1, word2, corr_ans in correct_ans:
        pred_ans = s.arrayStringsAreEqualNoSpace(word1, word2)
        assert (pred_ans == corr_ans), f"For {word1} and {word2}, got answer {pred_ans}, expected {corr_ans}"
    print('All tests for arrayStringsAreEqualNoSpace passed')
