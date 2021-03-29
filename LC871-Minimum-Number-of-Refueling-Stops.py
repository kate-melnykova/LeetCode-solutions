"""
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents
a gas station that is station[i][0] miles east of the starting
position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has
startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile
that it drives.

When the car reaches a gas station, it may stop and refuel,
transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in
order to reach its destination?  If it cannot reach the destination,
return -1.

Note that if the car reaches a gas station with 0 fuel left, the car
can still refuel there.  If the car reaches the destination with 0
fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


Note:
1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
"""
from typing import List
import bisect


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        unused_gas = list()
        n_used_stations = 0
        cur_fuel = startFuel
        for loc, fuel in stations:
            while cur_fuel < loc and unused_gas:
                cur_fuel += unused_gas.pop()  # get gas from the station that has the largest gas amount
                n_used_stations += 1
            if cur_fuel < loc:
                return -1

            # add fuel to the unused_gas
            bisect.insort(unused_gas, fuel)

        # get to the target
        while cur_fuel < target and unused_gas:
            cur_fuel += unused_gas.pop()  # get gas from the station that has the largest gas amount
            n_used_stations += 1
        if cur_fuel < target:
            return -1

        return n_used_stations


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [1, 1, [], 0],
        [100, 1, [[10, 100]], -1],
        [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2],
        [1000, 83, [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]], -1]
    ]
    print(f"Running tests for minRefuelStops")
    run_tests.run_tests(Solution().minRefuelStops, correct_answers)