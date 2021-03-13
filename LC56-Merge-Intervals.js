/*
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of
the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4
 */

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    // Runtime complexity: O(n) - we pass the array once
    // Space complexity: O(n)
    intervals.sort((a, b) => a[0] - b[0])
    var ans = new Array();
    var start = intervals[0][0];
    var end = intervals[0][1];
    for (let i=1; i < intervals.length; i++){
        if (end < intervals[i][0]){
            ans.push([start, end])
            start = intervals[i][0];
            end = intervals[i][1];
        } else if (intervals[i][1] > end){
            end = intervals[i][1];
        }
    };
    ans.push([start, end]);
    return ans
};