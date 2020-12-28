"""
Reach a Number, Leetcode problem 754,
https://leetcode.com/problems/reach-a-number/

You are standing at position 0 on an infinite number line.
There is a goal at position target.

On each move, you can either go left or right.
During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        if target < 6:
            return [0, 1, 3, 2, 3, 5, 3][target]
        sum_ = 0
        steps = 0
        while sum_ < target:
            steps += 1
            sum_ += steps
        if sum_ == target or not (sum_ - target) % 2:
            return steps

        if steps % 2:
            return steps + 2
        else:
            return steps + 1

# Runtime complexity O(log(target)) - number of times while loops will iterate
# Space complexity O(1)


if __name__ == "__main__":
    s = Solution()
    assert(s.reachNumber(0) == 0), f'Testcase for target = 0 failed: expected 0, got {s.reachNumber(0)}'
    assert (s.reachNumber(1) == 1), f'Testcase for target = 1 failed: expected 1, got {s.reachNumber(1)}'
    assert (s.reachNumber(2) == 3), f'Testcase for target = 2 failed: expected 3, got {s.reachNumber(2)}'
    assert (s.reachNumber(3) == 2), f'Testcase for target = 3 failed: expected 2, got {s.reachNumber(3)}'
    assert (s.reachNumber(100000000) == 14143), f'Testcase for target = 100000000 failed: expected 14143, got {s.reachNumber(100000000)}'
    assert (s.reachNumber(100000001) == 14142), f'Testcase for target = 100000001 failed: expected 14142, got {s.reachNumber(100000001)}'

