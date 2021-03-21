"""
You are given three positive integers n, index and maxSum.
You want to construct an array nums (0-indexed) that
satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:
Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the
conditions. There are no other valid arrays with a larger value
at the given index.

Example 2:
Input: n = 6, index = 1,  maxSum = 10
Output: 3


Constraints:
1 <= n <= maxSum <= 10^9
0 <= index < n
"""


class Solution:
    def total(self, x: int):
        i = self.index
        if x <= i:
            left_sum = x * (x - 1) // 2
        else:
            left_sum = i * x - (i * (i + 1) // 2)

        if x <= self.n - 1 - i:
            right_sum = x * (x - 1) // 2
        else:
            right_sum = (self.n - 1 - i) * x - ((self.n - 1 - i) * (self.n - i) // 2)
        # print(x, left_sum, right_sum)
        return left_sum + x + right_sum

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.n = n
        self.index = index
        maxSum -= n
        self.maxSum = maxSum
        min_ = 0
        max_ = maxSum
        while min_ + 1 < max_:
            guess = (min_ + max_) // 2
            if self.total(guess) <= maxSum:
                min_ = guess
            else:
                max_ = guess

        if self.total(max_) <= maxSum:
            return max_ + 1
        else:
            return min_ + 1


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [4,2,6,2],
        [6,1,10,3]
    ]
    run_tests(Solution().maxValue, correct_answers)