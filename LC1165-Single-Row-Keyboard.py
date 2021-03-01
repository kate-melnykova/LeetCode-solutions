"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of
the keyboard (indexed from 0 to 25), initially your finger is
at index 0. To type a character, you have to move your finger
to the index of the desired character. The time taken to move
your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate
how much time it takes to type it with one finger.

Example 1:
Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1
to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4.

Example 2:
Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73


Constraints:
(*) keyboard.length == 26
(*) keyboard contains each English lowercase letter exactly once in some order.
(*) 1 <= word.length <= 10^4
(*) word[i] is an English lowercase letter.
"""


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        Runtime complexity: O(n)
        Space complexity: O(n)
        """
        locations = {key: i for i, key in enumerate(keyboard)}
        loc = 0

        dist = 0
        for char in word:
            dist += abs(loc - locations[char])
            loc = locations[char]
        return dist

    def calculateTimeNoSpace(self, keyboard: str, word: str) -> int:
        """
        Runtime complexity: O(n^2)
        Space complexity: O(1)
        """
        self.keyboard = keyboard
        loc = 0

        dist = 0
        for char in word:
            new_loc = self._get_loc(char)
            dist += abs(loc - new_loc)
            loc = new_loc
        return dist

    def _get_loc(self, char: str):
        return self.keyboard.index(char)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        ["abcdefghijklmnopqrstuvwxyz", "cba", 4],
        ["pqrstuvwxyzabcdefghijklmno", "leetcode", 73]
    ]
    methods = ['calculateTime', 'calculateTimeNoSpace']

    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)