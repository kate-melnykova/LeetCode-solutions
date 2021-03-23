"""
Given a wordlist, we want to implement a spellchecker that converts a query
word into a correct word.

For a given query word, the spell checker handles two categories of spelling
mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive),
then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the
query word with any vowel individually, it matches a word in the wordlist
(case-insensitive), then the query word is returned with the same case as the
match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you
should return the same word back.
When the query matches a word up to capitlization, you should return the first
such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first
such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the
correct word for query = queries[i].


Example 1:
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite",
"KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]


Note:
1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
"""
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_lower = dict()  # key = lowercase word, value = List[such words]
        vowel_agnostic = dict()  # key = encoded lowercase word, value = the first appearance in the wordList
        for word in wordlist:
            words_lower[word.lower()] = words_lower.get(word.lower(), []) + [word, ]
            word_enc = self.encode(word.lower())
            if word_enc not in vowel_agnostic:
                vowel_agnostic[word_enc] = word

        response = []
        for q in queries:
            q_lower = q.lower()
            if q in words_lower.get(q_lower, []):
                response.append(q)
            elif q_lower in words_lower:
                response.append(words_lower[q_lower][0])
            else:
                q_enc = self.encode(q_lower)
                if q_enc in vowel_agnostic:
                    response.append(vowel_agnostic[q_enc])
                else:
                    response.append('')
        return response

    def encode(self, s: str) -> str:
        return s.replace('a', '*').replace('o', '*').replace('e', '*').replace('i', '*').replace('u', '*')


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [["yellow", ], ["YellOw", ], ["yellow", ]],
        [["Yellow", ], ["yellow", ], ["Yellow", ]],
        [["yellow", ], ["yellow", ], ["yellow", ]],
        [["KiTe", "kite", "hare", "Hare"],
         ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"],
         ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]]
    ]
    print(f'Running tests for spellchecker')
    run_tests.run_tests(Solution().spellchecker, correct_answers)
