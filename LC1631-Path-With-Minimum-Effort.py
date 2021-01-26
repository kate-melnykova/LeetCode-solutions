"""
You are a hiker preparing for an upcoming hike. You are given heights,
a 2D array of size rows x columns, where heights[row][col] represents
the height of cell (row, col). You are situated in the top-left cell,
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1)
(i.e., 0-indexed). You can move up, down, left, or right, and you wish
to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between
two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to
the bottom-right cell.

Example 1.
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of
1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:
(*) rows == heights.length
(*) columns == heights[i].length
(*) 1 <= rows, columns <= 100
(*) 1 <= heights[i][j] <= 106
"""
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Find the minimum effort required to get from top-left corner of heights to lower-right
        :param heights: rectangular-like map represented as list of lists
        :return: the minimum effort required

        Time complexity: O(mn * log(var)), where the heights is m-by-n board and var
        is the spread of values in heights
        Space complexity: O(mn)
        """
        self.heights = heights
        min_ = 0
        max_ = max(max(row) for row in heights) - min(min(row) for row in heights)
        # find the largest acceptable height diff using the binary search on effort
        while min_ < max_:
            guess = (min_ + max_) // 2
            if self.verifyIsPossible(guess):
                max_ = guess
            else:
                min_ = guess + 1
        return max_

    def verifyIsPossible(self, effort: int) -> bool:
        """
        verify if it is possible get from the top left corner to the
        bottom right corner of the heights while having only pre-determined
        effort
        :param effort: the max available effort
        :return: if there is a path that is achievable given the effort

        Time complexity: O(mn)
        Space complexity: O(mn)
        """
        rec = [(0, 0), ]
        attainable = set(rec)
        got_to_the_end = False
        while rec and not got_to_the_end:
            x, y = rec.pop()

            h = self.heights[x][y]
            # up
            if x > 0 and abs(self.heights[x - 1][y] - h) <= effort and (x - 1, y) not in attainable:
                rec.append((x - 1, y))
                attainable.add((x - 1, y))
            # down
            if x + 1 < len(self.heights) and abs(self.heights[x + 1][y] - h) <= effort and (x + 1, y) not in attainable:
                rec.append((x + 1, y))
                attainable.add((x + 1, y))
            # left
            if y > 0 and abs(self.heights[x][y - 1] - h) <= effort and (x, y - 1) not in attainable:
                rec.append((x, y - 1))
                attainable.add((x, y - 1))
            # right
            if y + 1 < len(self.heights[0]) and abs(self.heights[x][y + 1] - h) <= effort and (x, y + 1) not in attainable:
                rec.append((x, y + 1))
                attainable.add((x, y + 1))
            if (len(self.heights) - 1, len(self.heights[0]) - 1) in attainable:
                return True
        return False


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[[1,2,2],[3,8,2],[5,3,5]], 2],
        [[[1,2,3],[3,8,4],[5,3,5]], 1],
        [[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0],
        [[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,2]], 1]
    ]
    print('Running tests for minimumEffortPath')
    run_tests(Solution().minimumEffortPath, correct_answers)