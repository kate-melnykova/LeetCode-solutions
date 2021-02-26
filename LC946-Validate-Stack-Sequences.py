"""
Given two sequences pushed and popped with distinct values, return true if
and only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.


Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:
(*) 0 <= pushed.length == popped.length <= 1000
(*) 0 <= pushed[i], popped[i] < 1000
(*) pushed is a permutation of popped.
(*) pushed and popped have distinct values.
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Runtime complexity: O(n)
        Space complexity: O(n)
        """
        i_popped = 0
        i_pushed = 0
        stack = list()
        while i_pushed < len(pushed):
            # we may keep pushing
            # check if popping is possible
            if stack and i_popped < len(popped) and stack[-1] == popped[i_popped]:
                stack.pop()
                i_popped += 1
            else:
                stack.append(pushed[i_pushed])
                i_pushed += 1

        while i_popped < len(popped):
            if not stack or stack[-1] != popped[i_popped]:
                return False

            stack.pop()
            i_popped += 1
        return True


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,2,3,4,5], [4,5,3,2,1], True],
        [[1,2,3,4,5], [4,3,5,1,2], False],
        [[1,2,3,4,5], [4,3,5,2,1], True],
        [[1,2,3,4,5], [4,5,3,1,2], False]
    ]
    methods = ['validateStackSequences', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)
