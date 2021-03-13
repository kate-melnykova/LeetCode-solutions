/*
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
(*) 1 <= a.length, b.length <= 10^4
(*) a and b consist only of '0' or '1' characters.
(*) Each string does not contain leading zeros except for the zero itself.
 */

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    // Runtime: O(n + m), Space: O(min(n+m))
    var over = 0;
    var i = 1;
    const len_a = a.length;
    const len_b = b.length;
    var sum_, dig_a, dig_b;
    var ans = '';
    while ((len_a >= i) | (len_b >= i) | (over > 0)){
        dig_a = len_a < i ? 0 : parseInt(a[len_a - i]);
        dig_b = len_b < i ? 0 : parseInt(b[len_b - i]);
        sum_ = dig_a + dig_b + over;
        if (sum_ > 1){
            over = 1;
            sum_ = sum_ - 2;
        } else {
            over = 0;
        };
        ans = sum_.toString() + ans;
        i ++;
    }
    return ans
};