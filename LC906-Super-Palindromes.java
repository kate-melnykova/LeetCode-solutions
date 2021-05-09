/*
Let's say a positive integer is a super-palindrome if it is a palindrome,
and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the
number of super-palindromes integers in the inclusive range [left, right].

Example 1:
Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

Example 2:
Input: left = "1", right = "2"
Output: 1


Constraints:
- 1 <= left.length, right.length <= 18
- left and right consist of only digits.
- left and right cannot have leading zeros.
- left and right represent integers in the range [1, 10^18].
- left is less than or equal to right.
*/


class Solution {
    public int superpalindromesInRange(String left, String right) {
        long leftNum = Long.parseLong(left);
        long rightNum = Long.parseLong(right);
        int halfNum;

        int count = 0;
        int maxHalf = 1000000000;
        String num;
        long n;

        // try all even-length palindromes
        for (int i=1; i < maxHalf; i++){
            num = Long.toString(i);
            StringBuilder sb = new StringBuilder(num);
            int length = sb.length();
            for (int j=length-1; j >= 0; j--){
                sb.append(num.charAt(j));
            }
            num = sb.toString();
            n = Long.parseLong(sb.toString());
            n *= n;
            if (n > rightNum){
                break;
            }
            if ((n >= leftNum) && (n <= rightNum) && isPalindrome(n)){
                count++;
            }
        }
        // try all odd-length palindromes
        for (long i=1; i < maxHalf; i++){
            num = Long.toString(i);
            StringBuilder sb = new StringBuilder(num);
            int length = sb.length();
            for (int j=length-2; j >= 0; j--){
                sb.append(num.charAt(j));
            }
            num = sb.toString();
            n = Long.parseLong(sb.toString());
            n *= n;
            if (n > rightNum){
                break;
            }
            if ((n >= leftNum) && (n <= rightNum) && isPalindrome(n)){
                count++;
            }
        }
        return count;

    }

    private boolean isPalindrome(long n){
        String num = Long.toString(n);
        int i = 0;
        int j = num.length()-1;
        while (i < j){
            if (num.charAt(i) != num.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}