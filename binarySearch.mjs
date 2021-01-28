/**
Find the first idx such that arr[idx] >= n
If there is no such idx, return arr.length
 * @param {number[]} arr
 * @param {number} n
 * @return {number} index of the insertion of element n into sorted arr
**/
function binarySearch(arr, n){
    if (arr.length == 0){
        return 0
    } else if (arr[arr.length - 1] < n){
        return arr.length
    }
c
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

export { binarySearch };