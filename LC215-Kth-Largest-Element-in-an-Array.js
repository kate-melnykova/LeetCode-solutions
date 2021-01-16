/**
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
**/
console.log('Current directory: ' + process.cwd());
/* import binarySearch from "./binarySearch.mjs"; */

function binarySearch(arr, n){
    if (arr.length == 0){
        return 0
    } else if (arr[arr.length - 1] < n){
        return arr.length
    }

    let i_min = 0;
    let i_max = arr.length - 1;
    let guess;
    while (i_min + 1 < i_max){
        guess = ~~((i_min + i_max + 1) / 2);
        if (arr[guess] <= n){
            i_min = guess + 1;
        } else {
            i_max = guess;
        }
    }

    if (arr[i_min] > n){
        return i_min
    } else {
        return i_max
    }
}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

var findKthLargest = function(nums, k) {
    var arr = new Array();
    let idx;
    for (let n of nums){
        if (arr.length == 0){
            arr.push(n);
        } else {
            idx = binarySearch(arr, n);
            if ((arr.length < k)){
                arr.splice(idx, 0, n);
            } else if (idx > 0){
                arr.splice(idx, 0, n);
                arr.shift();
            };
        };
    };
    return arr[0]
};