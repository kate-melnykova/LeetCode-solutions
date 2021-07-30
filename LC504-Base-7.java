/*
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:
-10^7 <= num <= 10^7
*/

class Solution {
    public String convertToBase7(int num) {
        StringBuilder sb = new StringBuilder();
        boolean isPositive = true;
        if (num < 0){
            isPositive = false;
            num = -num;
        }
        while (num >= 7){
            sb.append(num % 7);
            num = num / 7;
        }
        sb.append(num);
        if (!isPositive){
            sb.append('-');
        }
        return sb.reverse().toString();
    }
}