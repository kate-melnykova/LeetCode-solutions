"""
You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums.



Example 1:

Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
Example 2:

Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0],
nums[1], and nums[2] is 1.
Example 3:

Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0],
nums[1], nums[2], and nums[3] is 2.


Constraints:
0 <= n <= 100
"""
from run_tests import run_tests


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        Generate the array as described above and dynamically find the max
        :param n: the length of the target array
        :return: max value
        """
        memo = {0: 0, 1: 1}
        if n < 2:
            return memo[n]

        max_val = 0
        for i in range(2, n + 1):
            if not i % 2:
                memo[i] = memo[i // 2]
            else:
                memo[i] = memo[i // 2] + memo[(i + 1) // 2]
            max_val = max(max_val, memo[i])
        return max_val


if __name__ == "__main__":
    """
    f(2) = f(1)
        f(3) = f(2) + f(1) = 2f(1)
        f(4) = f(1)
        f(5) = f(2) + f(3) = 3f(1)
        f(6) = f(3) = 2f(1)
        f(7) = f(3) + f(4) = 3f(1)
        f(8) = f(1)
        f(9) = f(4) + f(5) = 4f(1)
        f(10) = 3f(1)
        f(11) = 5f(1)
        f(12) = 2f(1)
        f(13)= 5f(1)
        f(14) = f(7) = 3f(1)
        f(15) = 4f(1)
    """
    correct_answers = [
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 2],
        [7, 3],
        [15, 5],
        [100, 21]
    ]
    print('Starting tests for getMaximumGenerated')
    run_tests(Solution().getMaximumGenerated, correct_answers)