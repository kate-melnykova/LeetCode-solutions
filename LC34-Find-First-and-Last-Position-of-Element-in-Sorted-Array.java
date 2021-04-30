/*
Given an array of integers nums sorted in ascending order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
*/

class Solution {
    public int[] searchRange(int[] nums, int target) {
        // Runtime complexity: O(log n)
        // Space complexity: O(1)
        if ((nums == null) | (nums.length == 0)){
            return new int[] {-1, -1};
        }
        // find the first occurence of target
        int iMin = 0;
        int iMax = nums.length - 1;
        int guess;
        while (iMin < iMax){
            guess = (iMin + iMax) / 2;
            if (nums[guess] < target){
                iMin = guess + 1;
            } else {
                iMax = guess;
            }
        }
        int firstIndex = iMin;
        if (nums[firstIndex] != target){
            return new int[] {-1, -1};
        }

        //get the last occurence
        iMax = nums.length - 1;
        while (iMin < iMax){
            guess = (iMin + iMax + 1) / 2;
            if (nums[guess] <= target){
                iMin = guess;
            } else {
                iMax = guess - 1;
            }
        }
        return new int[] {firstIndex, iMin};
    }
}