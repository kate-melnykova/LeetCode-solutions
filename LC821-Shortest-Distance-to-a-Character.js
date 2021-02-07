/*
Given a string s and a character c that occurs in s, return an
array of integers answer where answer.length == s.length and
answer[i] is the shortest distance from s[i] to the character c in s.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]


Constraints:
(*) 1 <= s.length <= 104
(*) s[i] and c are lowercase English letters.
(*) c occurs at least once in s.
 */

/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    let shortestDist = new Array();
    let rightDist = 10000;
    for (let i=0; i < s.length; i ++){
        if (s[i] == c){
            rightDist = 0;
        } else {
            rightDist ++;
        };
        shortestDist.push(rightDist);
    };
    let leftDist = 10000;
    for (let i=s.length-1; i >= 0; i --){
        if (s[i] == c){
            leftDist = 0;
        } else {
            leftDist ++;
        };
        if (shortestDist[i] > leftDist){
            shortestDist[i] = leftDist;
        };
    };
    return shortestDist
};

if (typeof require !== 'undefined' && require.main === module) {
    const correct_answers = [
        ["loveleetcode", "e", [3,2,1,0,1,0,0,1,2,2,1,0]],
        ["aaab", "b", [3,2,1,0]]
    ];
    console.log('Running tests for shortestToChar');
    let ans, pred;
    for (let i = 0; i < correct_answers.length; i++){
        ans = correct_answers[i].pop();
        pred = shortestToChar(correct_answers[i][0], correct_answers[i][1]);
        console.assert(ans.length === pred.length && ans.every(function(value, index) { return value === pred[index]}),
            'For input %s, got answer %s, expected %s',
            correct_answers[i], pred, ans)
    };
    console.log('All tests done')

}