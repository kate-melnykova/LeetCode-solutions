"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0  # stores the max length of substring found so far
        memo = {}  # the last occurence of each character (so far)
        i_slow = -1  # the beginning of the longest substring
        # i represents the last index of the currently considered substring
        for i, char in enumerate(s):
            i_slow = max(i_slow, memo.get(char, -1))
            max_len = max(max_len, i - i_slow)
            memo[char] = i
        return max(max_len, i - i_slow)


if __name__ == '__main__':
    s = Solution()
    answers = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3,
        "": 0
    }
    for word, answer in answers.items():
        ans_pred = s.lengthOfLongestSubstring(word)
        assert(ans_pred == answer), f'For substring {word}, got answer {ans_pred}, expected {answer}'
