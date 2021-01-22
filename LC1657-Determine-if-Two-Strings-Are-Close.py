"""
Two strings are considered close if you can attain one from
the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character
into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2
are close, and false otherwise.



Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Example 4:
Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.


Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        determine if word1 and word2 are similar by the rules described above

        The idea is based on the fact that each word can be rearranged to be sorted
        according to the number of occurences of each letter. For example,
        aua -> uaa
        babc ->acbb or cabb
        Note that operations 1 and 2 do not change the overall frequency distribution and
        the set of letters used. If frequency distribution and set of letters used matched,
        then sorted words may be converted to each other.

        Time complexity: O(nlog n)
        Space complexity: O(n)
        """
        if len(word1) != len(word2):
            return False

        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and list(sorted(c1.values())) == list(sorted(c2.values()))


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ['abc', 'bca', True],
        ['aa', 'a', False],
        ['cabbba', 'abbccc', True],
        ['cabbba', 'aabbss', False],
        ['aab', 'ccb', False]
    ]
    methods = ['closeStrings', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)
