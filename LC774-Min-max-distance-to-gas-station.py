"""
On a horizontal number line, we have gas stations at positions stations[0],
stations[1], ..., stations[N-1], where N = stations.length.
Now, we add K more gas stations so that D, the maximum distance between
adjacent gas stations, is minimized.
Return the smallest possible value of D.
Example:
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:
(1) stations.length will be an integer in range [10, 2000].
(2) stations[i] will be an integer in range [0, 10^8].
(3) K will be an integer in range [1, 10^6].
(4) Answers within 10^-6 of the true value will be accepted as correct.
"""
from typing import List
import math

from run_tests import run_tests_approx


class Solution:
    def min_max_distance_to_gas_station(self, stations: List[int], k: int) -> float:
        if len(stations) < 2:
            return 0.0

        self.stations = stations
        self.stations.sort()
        self.k = k
        self.small_number = 10 ** (-9)
        delta = 0.5 * (10 ** (-6))
        min_distance = float(10 ** (-7))
        max_distance = float(self.stations[-1] - self.stations[0] - self.small_number) / k
        while min_distance + delta < max_distance:
            guess = (min_distance + max_distance) / 2
            if self.can_fit(guess):
                max_distance = guess
            else:
                min_distance = guess
        return min_distance


    def can_fit(self, max_dist: float) -> bool:
        """
        Determines if it is possible to add k gas stations to existing stations such that
        the distances between consecutive stations is at most max_dist
        :param max_dist: max distance allowed between consecutive stations
        :return: if it is possible to add k gas stations as described above
        Runtime comlexity: O(len(stations))
        Space complexity: O(1)
        """
        return sum(math.floor((self.stations[i] - self.stations[i-1] - self.small_number) / max_dist) \
                   for i in range(1, len(self.stations))) <= self.k


if __name__ == "__main__":
    correct_answers = [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 0.5],
        [[1, 2], 3, 0.25],
        [[1, 2], 4, 0.2],
        [[1, 2, 102], 9, 10.0]
    ]
    methods = ['min_max_distance_to_gas_station']
    for method in methods:
        print(f'Running tests for {method}')
        run_tests_approx(getattr(Solution(), method), correct_answers, 10 ** (-6))