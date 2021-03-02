"""
A group of two or more people wants to meet and minimize the total travel
distance. You are given a 2D grid of values 0 or 1, where each 1 marks
the home of someone in the group. The distance is calculated using Manhattan
Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:
Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6
Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
"""
from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Runtime complexity: O(nm) -- need to go over the grid once
        Space complexity: O(n + m)
        """
        # Manhettan distance, as a partial case of L1 norm,
        # is separable. We can proceed each coordinate individually
        agg_x = [0] * len(grid)
        agg_y = [0] * len(grid[0])
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item:
                    agg_x[i] += 1
                    agg_y[j] += 1

        dist_x_min = float('inf')
        houses_to_left = 0
        dist_left = 0
        houses_to_right = sum(agg_x)
        dist_right = sum((i + 1) * x for i, x in enumerate(agg_x))
        for i, houses_cur in enumerate(agg_x):
            # move houses from the right to current loc
            dist_right -= houses_to_right
            houses_to_right -= houses_cur
            dist_x_min = min(dist_x_min, dist_left + dist_right)
            houses_to_left += houses_cur
            dist_left += houses_to_left

        dist_y_min = float('inf')
        houses_upper = 0
        dist_upper = 0
        houses_down = sum(agg_y)
        dist_down = sum((i + 1) * y for i, y in enumerate(agg_y))
        for j, houses_cur in enumerate(agg_y):
            # move houses from the down to current loc
            dist_down -= houses_down
            houses_down -= houses_cur
            dist_y_min = min(dist_y_min, dist_upper + dist_down)
            houses_upper += houses_cur
            dist_upper += houses_upper
        return dist_x_min + dist_y_min


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[[1,0,0,0,1],[1,0,0,0,0],[1,0,1,0,0]], 10],
        [[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]], 6]
    ]
    print(f'Running tests for minTotalDistance')
    run_tests(Solution().minTotalDistance, correct_answers)