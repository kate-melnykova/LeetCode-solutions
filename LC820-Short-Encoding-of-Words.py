"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i]
and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference
string s possible of any valid encoding of words.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and
indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to
the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the
next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to
the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].

Constraints:
(*) 1 <= words.length <= 2000
(*) 1 <= words[i].length <= 7
(*) words[i] consists of only lowercase letters.
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        total_length = 0
        encoded_words = set()
        for i, word in enumerate(words):
            if all(not encoded.endswith(word) for encoded in encoded_words):
                encoded_words.add(word)
                total_length += len(word) + 1

        return total_length

if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [["time", "me", "bell"], 10],
        [["time", "me", "bell", "cell"], 15],
        [["me", "time", "bell"], 10]
    ]
    print(f'Running tests for minimumLengthEncoding')
    run_tests(Solution().minimumLengthEncoding, correct_answers)