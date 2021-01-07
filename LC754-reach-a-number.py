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
    """
    You are standing at position 0 on an infinite number line.
     There is a goal at position target.

    On each move, you can either go left or right. During
    the n-th move (starting from 1), you take n steps.

    Return the minimum number of steps required to reach the destination.

    https://leetcode.com/problems/reach-a-number/
    """
    def reachNumber(self, target: int) -> int:
        # observe that moving rules are symmetric, and therefore,
        # the number of steps required to reach target and -target is identical
        # WLOG, assume that target is non-negative
        target = abs(target)
        if target < 6:
            return [0, 1, 3, 2, 3, 5, 3][target]

        # let's start from lower bound
        # we need at least n numbers where
        # 1 + 2 + ... + n >= target
        # we may need more numbers, but such n gives us a lower estimate
        sum_ = 0
        n = 0
        while sum_ < target:
            n += 1
            sum_ += n
        # Now, let's refine the estimate
        # if we found such n, we have a few cases
        # (a) 1 + 2 +  ... + n = target
        # in this case, the minimum number of integers is n
        # (b) 1 + 2 + ... + n - target is even
        # in this, case, let i = (1 + 2 + ... + n - target) / 2
        # then, 1 + 2 + ... + (i-1) - i + (i+1) + (i+2) + ... + n = 1 + 2 + ... + n - 2i = target
        # and, therefore, the answer is n
        if sum_ == target or not (sum_ - target) % 2:
            return n
        # (c) 1 + 2 + ... + n - target is odd
        # first, observe that n numbers is not enough
        # Indeed, if we put '-' in front of some numbers, then the result will have different
        # oddity from target
        # Therefore, we add n+1. If (1+2+...+ (n+1)) - target is even, then the answer is n+1 (as discussed above)
        # If (1 + 2 + ... (n+1)) is odd, we need to add one more number.
        # Note that (1+2+...+ n - target) and (1 +2 + ... + (n+1) - target) are both odd if (n+1) is even,
        # i.e., when n is odd. Adding n+2 will change the oddity, and therefore, it is the answer
        # Simplifying all of above, we get
        return n + 1 + n % 2

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

