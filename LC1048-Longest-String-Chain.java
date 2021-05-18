/*
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add
exactly one letter anywhere in word1 to make it equal to word2. For
example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k]
with k >= 1, where word_1 is a predecessor of word_2, word_2 is a
predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen
from the given list of words.



Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
*/

class Solution {
    HashMap<String, Integer> memo = new HashMap<String, Integer>();
    HashMap<Integer, HashSet<String>> levels = new HashMap<Integer, HashSet<String>>();
    public int longestStrChain(String[] words) {
        HashSet<String> wordsLevel;
        for (int i = 0; i < words.length; i++){
            int length = words[i].length();
            if (levels.containsKey(length)){
                wordsLevel = levels.get(length);
            } else {
                wordsLevel = new HashSet<String>();
                levels.put(length, wordsLevel);
            }
            wordsLevel.add(words[i]);
        }
        int maxDepth = 0;
        int depth;
        for (int i=0; i < words.length; i++){
            depth = getDepth(words[i]);
            maxDepth = Math.max(maxDepth, depth);
        }
        return maxDepth;
    }

    private int getDepth(String word){
        if (memo.containsKey(word)){
            return memo.get(word);
        }

        int level = word.length();
        if (level == 1 || !levels.containsKey(level-1)){
            return 1;
        }
        HashSet oneBelow = levels.get(level-1);
        String substring;
        int depth;
        int maxDepth = 1;
        for (int i=0; i < level; i++){
            substring = word.substring(0,i) + word.substring(i+1, level);
            if (oneBelow.contains(substring)){
                depth = getDepth(substring) + 1;
                maxDepth = Math.max(maxDepth, depth);
            }
        }
        memo.put(word, maxDepth);
        return maxDepth;
    }
}