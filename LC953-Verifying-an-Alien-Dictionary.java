/*
In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order. The order of the alphabet is some
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of
the alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then
words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second
string is shorter (in size.) According to lexicographical rules
"apple" > "app", because 'l' > '∅', where '∅' is defined as the blank
character which is less than any other character (More info).


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
*/

class Solution {
    HashMap<Character, Integer> letterToOrder;
    public boolean isAlienSorted(String[] words, String order) {
        this.letterToOrder = new HashMap<Character, Integer>();
        for (int i = 0; i < order.length(); i++){
            this.letterToOrder.put(order.charAt(i), i);
        }

        for (int i = 1; i < words.length; i ++){
            if (!compareStrings(words[i-1], words[i])){
                return false;
            }
        }
        return true;
    }

    private boolean compareStrings(String firstWord, String secondWord){
        int l1 = firstWord.length();
        int l2 = secondWord.length();

        int i = 0;
        while ((i < l1) && (i < l2) && (firstWord.charAt(i) == secondWord.charAt(i))){
            i ++;
        }

        // check if one of the words has no more chars after index i
        if (i == l1){
            return true;
        } else if (i == l2){
            return false;
        }

        char char1 = firstWord.charAt(i);
        char char2 = secondWord.charAt(i);
        int idx1 = this.letterToOrder.get(char1);
        int idx2 = this.letterToOrder.get(char2);
        if (this.letterToOrder.get(char1) < this.letterToOrder.get(char2)){
            return true;
        } else {
            return false;
        }
    }
}