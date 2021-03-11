"""
You are given coins of different denominations and a total amount of
money amount. Write a function to compute the fewest number of coins
that you need to make up that amount. If that amount of money cannot
be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2


Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        coins = list(filter(lambda x: x <= amount, coins))
        if not coins:
            return -1

        max_coin = max(coins)
        dp = [float('inf'), ] * max_coin
        dp[0] = 0
        for n in range(amount):
            # we can get n coins that by dp[0] steps
            # then, it is possible to get (n + coin) coins with dp[0]+1 coins, where coin is one of the coin amounts
            n_coins = dp.pop(0)
            dp.append(float('inf'))
            # then, 0-indexed entry corresponds to n+1 coins, 1-indexed - for n+2 coins, etc.
            for coin in coins:
                dp[coin - 1] = min(dp[coin - 1], n_coins + 1)
        return dp[0] if dp[0] < float('inf') else -1


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1, 2, 5], 11, 3],
        [[2, 5], 6, 3],
        [[12356], 2, -1],
        [[123456], 0, 0],
        [[7, 5], 8, -1]
    ]
    print(f'Running tests for coinChange')
    run_tests(Solution().coinChange, correct_answers)