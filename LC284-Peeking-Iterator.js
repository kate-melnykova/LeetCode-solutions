/*
Given an Iterator class interface with methods: next() and hasNext(),
design and implement a PeekingIterator that support the peek() operation
-- it essentially peek() at the element that will be returned by the
next call to next().

Example:
Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?
 */


/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    };
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
   this.data = iterator;
    this.nextItem = null;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    if (this.nextItem===null){
        this.nextItem = this.data.next();
    };
    return this.nextItem
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    if (this.nextItem === null){
        var n = this.data.next();
    } else {
        var n = this.nextItem;
        this.nextItem = null;
    };
    return n
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    if (this.nextItem === null){
        return (this.data.hasNext())
    } else {
        return true
    }
};

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(arr)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */