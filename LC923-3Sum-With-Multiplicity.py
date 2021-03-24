"""
Given an integer array arr, and an integer target, return the
number of tuples i, j, k such that i < j < k and
arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:
(*) 3 <= arr.length <= 3000
(*) 0 <= arr[i] <= 100
(*) 0 <= target <= 300
"""
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        modulo = 10 ** 9 + 7
        return sum(self.twoSumMulti(arr, i, target - arr[i]) % modulo for i in range(len(arr) - 2)) % modulo

    def twoSumMulti(self, arr: List[int], i: int, target: int) -> int:
        j = i + 1
        k = len(arr) - 1
        mult_j = 0
        mult_k = 0
        t = target - arr[i]
        ans = 0
        while j < k:
            if arr[j] + arr[k] < target:
                j += 1
            elif arr[j] + arr[k] > target:
                k -= 1
            else:
                mult_j = 1
                mult_k = 1
                while j + 1 < k and arr[j] == arr[j + 1]:
                    mult_j += 1
                    j += 1
                while j < k - 1 and arr[k] == arr[k - 1]:
                    mult_k += 1
                    k -= 1
                if arr[j] == arr[k]:
                    # we covered all the array
                    mult = mult_j + mult_k
                    return ans + (mult * (mult - 1)) // 2

                else:
                    ans += mult_j * mult_k
                    j += 1
                    k -= 1
        return ans


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20],
        [[1, 1, 2, 2, 2, 2], 5, 12]
    ]
    print(f'Running tests for threeSumMulti')
    run_tests.run_tests(Solution().threeSumMulti,
                        correct_answers)
