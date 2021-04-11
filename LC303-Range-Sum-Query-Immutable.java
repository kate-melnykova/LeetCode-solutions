/*
Given an integer array nums, find the sum of the elements between
indices left and right inclusive, where (left <= right).

Implement the NumArray class:

NumArray(int[] nums) initializes the object with the integer array nums.
int sumRange(int left, int right) returns the sum of the elements of
the nums array in the range [left, right] inclusive
(i.e., sum(nums[left], nums[left + 1], ... , nums[right])).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.
*/

class NumArray {
    int[] sums;

    public NumArray(int[] nums) {
        this.sums = new int[nums.length + 1];
        int sum = 0;
        for (int i=0; i < nums.length; i ++){
            sum = sum + nums[i];
            this.sums[i+1] = sum;
        }
    }

    public int sumRange(int left, int right) {
        return this.sums[right+1] - this.sums[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */