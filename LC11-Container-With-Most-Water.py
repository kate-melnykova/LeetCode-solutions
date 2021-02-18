"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis
forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2


Constraints:
(*) n == height.length
(*) 2 <= n <= 3 * 10^4
(*) 0 <= height[i] <= 3 * 10^4
"""
from typing import List


class Solution:
    def maxAreaDirect(self, height: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        max_area = 0
        for i, right in enumerate(height):
            for j in range(i):
                area = min(right, height[j]) * (i-j)
                max_area = max(max_area, area)
        return max_area

    def maxArea(self, height: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # the optimal area enclosed is bounded by the left and right pillars
        # find the candidates for them
        consider_for_left = []  # list of tuples (height, x-coord)
        for i, h in enumerate(height):
            # if one of the previous pillars were taller than the current,
            # choosing previous pillar will only increase the enclosed area
            if not consider_for_left or consider_for_left[-1][0] < h:
                consider_for_left.append((h, i))
        consider_for_right = []  # list of tuples (height, x-coord)
        for i, h in enumerate(reversed(height)):
            # going from right to left
            # if one of the previous pillars were taller than the current,
            # choosing previous pillar as the right pillar will only increase the enclosed area
            if not consider_for_right or consider_for_right[-1][0] < h:
                consider_for_right.append((h, len(height) - 1 - i))

        max_area = 0
        # we have the list of potential left pillars
        # inside the list, heights of pillars are increasing, and x-coords are increasing
        # potential right pillars: heights are increasing, x-coords are decreasing
        i_left = 0
        i_right = 0
        while i_left < len(consider_for_left) and i_right < len(consider_for_right) and consider_for_left[i_left][1] < \
                consider_for_right[i_right][1]:
            height_left = consider_for_left[i_left][0]
            x_left = consider_for_left[i_left][1]
            height_right = consider_for_right[i_right][0]
            x_right = consider_for_right[i_right][1]
            area = min(height_left, height_right) * (x_right - x_left)
            max_area = max(area, max_area)
            if height_left <= height_right:
                # all pillars in consider_for_right[i_right:] are taller or equal then consider_for_left[i_left]
                # therefore, if consider_for_left[i_left] is the optimal left pillar, then the enclosed area
                # is maximized when i_right is as above.
                # proceed to the next pillar in consider_for_left
                i_left += 1
            else:
                # all pillars in consider_for_left[i_left:] are taller or equal then consider_for_left[i_right]
                # therefore, if consider_for_left[i_right] is the optimal right pillar, then the enclosed area
                # is maximized when i_left is as above.
                # proceed to the next pillar in consider_for_right
                i_right += 1
        return max_area


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,8,6,2,5,4,8,3,7], 49],
        [[1, 1], 1],
        [[4,3,2,1,4], 16],
        [[1,2,1], 2]
    ]
    methods = ['maxArea', 'maxAreaDirect', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(),method), correct_answers)