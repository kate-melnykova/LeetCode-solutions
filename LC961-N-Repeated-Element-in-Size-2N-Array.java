/*
In a array A of size 2N, there are N+1 unique elements, and exactly one
of these elements is repeated N times.

Return the element repeated N times.

Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
*/


class Solution {
    public int repeatedNTimes(int[] A) {
        // Runtime complexity: O(n)
        // Space complexity: O(1)
        if (A.length < 4){
            return A[0];
        }
        int first = A[0];
        if (first == A[1]){
            return first;
        }
        int second = A[1];
        if ((A[2] == first) || (A[2] == second)){
            return A[2];
        }
        int third = A[2];
        for (int i = 3; i < A.length; i++){
            if ((A[i] == first) || (A[i] == second) || (A[i] == third)){
                return A[i];
            }
        first = second;
        second = third;
        third = A[i];
        }
        return -1;
    }
}