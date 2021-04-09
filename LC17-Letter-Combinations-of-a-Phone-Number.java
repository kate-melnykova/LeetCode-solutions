/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
*/

class Solution {
    Map<Character, String> map = Map.of(
        '2', "abc", '3', "def", '4', "ghi", '5', "jkl", '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<String>();
        if (digits.length() == 0){
            return ans;
        }
        ans.add("");
        List<String> new_ans;
        String mapped_to, prefix, c_new;
        int i, j, k;
        Character c;
        for (i = 0; i < digits.length(); i ++){
            c = digits.charAt(i);
            new_ans = new ArrayList<String>();
            mapped_to = this.map.get(c);
            for (j = 0; j < mapped_to.length(); j ++){
                c_new = Character.toString(mapped_to.charAt(j));
                for (k = 0; k < ans.size(); k ++){
                    prefix = ans.get(k);
                    String new_string = prefix + c_new;
                    new_ans.add(new_string);
                }
            }
            ans = new ArrayList<>(new_ans);;
        }
        return ans;
    }
}