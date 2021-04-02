"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp
of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter
in the sequence with the corresponding letter from the stamp.  You can make up to
10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then
you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp
must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the
left-most letter being stamped at each turn.  If the sequence is not possible to
stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could
return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible
to stamp within 10 * target.length moves.  Any answers specifying more than this
number of moves will not be accepted.

Example 1:
Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:
Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
"""
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        Think backwards:
        1. Find the last stamping -- should match stamp exactly
        Example: stamp = "abca" target = "aabcaca"
         > "a(abca)ca"
         This stamp can be done at the last step.
         Replace all letters with stars and take note of stamp_location
         > stamp_locs = [1] target = "a****ca"
        2. Try to match stamp to the target using wildcards - * can be replaced by any symbols
        Example (ctd): > "(a***)*ca"
        > stamp_locs = [0] + stamp_locs = [0, 1] target = "*****ca"

        "***(**ca)" -> stamp_locs = [3,0,1] target = "*******"
        Done.

        One scan to search -> (len(target) - len(stamp)) locations, compare strings of len(stamp)
        Need to do at most len(target) scans
        If t = len(target) and s = len(stamp)
        Runtime complexity: O((t - s)ts)
        Space complexity: O(t)
        """
        if len(stamp) > len(target):
            return list()

        self.stamp = stamp
        self.stamp_pattern = [[char, "*"] for char in stamp]
        self.target = list(target) # to make it mutable
        n_chars_to_change = len(target)
        sequence = []
        while n_chars_to_change:
            i = self.find_matching_stamp()
            if i < 0:
                return []

            # put stamp at location i
            sequence.append(i)
            # change letters in target
            j = 0
            while j < len(stamp):
                if self.target[i + j] != "*":
                    n_chars_to_change -= 1
                    self.target[i + j] = "*"
                j += 1

        sequence.reverse()
        return sequence

    def match_stamp(self, i: int) -> bool:
        """
        determines if target[i:i+len(stamp)] matches stamp
        note that all stars don't match stamp
        """
        j = 0
        is_letter = False
        while j < len(self.stamp) and self.target[i+j] in self.stamp_pattern[j]:
            if self.target[i + j] != "*":
                is_letter = True
            j += 1
        return j == len(self.stamp) and is_letter

    def find_matching_stamp(self) -> int:
        """
        returns the index where stamp matches target or -1 if there is no match
        """
        i = 0
        while i <= len(self.target) - len(self.stamp) and not self.match_stamp(i):
            i += 1
        return i if i <= len(self.target) - len(self.stamp) else -1


if __name__ == "__main__":
    from run_tests import run_tests

    correct_answers = [
        ["abc", "ababc", [0, 2]],
        ["abca", "aabcaca", [3,0,1]]
    ]
    print(f"Running tests for movesToStamp")
    run_tests(Solution().movesToStamp, correct_answers)