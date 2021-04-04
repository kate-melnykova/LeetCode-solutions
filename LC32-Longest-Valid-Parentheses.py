"""
You have a RecentCounter class which counts the number of recent requests within
a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in
milliseconds, and returns the number of requests that has happened in the past
3000 milliseconds (including the new request). Specifically, return the number of
requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than
the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


Constraints:
1 <= t <= 10^9
Each test case will call ping with strictly increasing values of t.
At most 10^4 calls will be made to ping.
"""


class Solution:
    bal_change = {
        "(": 1,
        ")": -1
    }

    def longestValidParentheses(self, s: str) -> int:
        """
        Runtime complexity: O(n) - we make a single pass over the string
        Space complexity: O(n) (worst case scenario)
        """
        memo = {0: -1}
        max_len = 0
        bal = 0
        for i in range(len(s)):
            # note the current balance and the length of the current subsequence
            bal += self.bal_change[s[i]]
            if bal < 0:
                # no string that starts before is pos
                bal = 0
                memo = {0: i}
            elif bal in memo:
                max_len = max(max_len, i - memo[bal])
                if bal + 1 in memo:
                    memo.pop(bal + 1)
            else:
                memo[bal] = i
            i += 1
        return max_len


if __name__ == "__main__":
    from run_tests import run_tests

    correct_answers = [
        ["(()", 2],
        ["()())", 4],
        [")()())", 4],
        ["", 0],
        ["()((()())"]
    ]
    print("Running tests for longestValidParentheses")
    run_tests(Solution().longestValidParentheses, correct_answers)