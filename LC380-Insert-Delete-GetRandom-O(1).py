"""
Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was
not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at
least one element exists when this method is called). Each element must have the same probability of
being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?


Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:
(*) -2^31 <= val <= 2^31 - 1
(*) At most 10^5 calls will be made to insert, remove, and getRandom.
(*) There will be at least one element in the data structure when getRandom is called.
"""

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.

        We store the reversed binary representation of the number in the trie-like structure
        Note that binary representations contains '0' and '1' only.

        For the chain of n operation, runtime is O(n)
        """
        self.end = False  # is there any number that ends here
        self.neg = None
        self.zeros = None
        self.ones = None
        self.freq = 0  # total number of elements in the trie

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.

        Time complexity: O(log val)
        Space complexity: O(1)
        """
        if self.contains(val):
            return False

        self.freq += 1
        if not val:
            self.end = True
            return True

        elif val < 0 and self.neg is None:
            self.neg = RandomizedSet()
            self.neg.insert(-val)
            return True

        elif val < 0:
            self.neg.insert(-val)
            return True

        char = val % 2
        val = val // 2

        if char == 0 and self.zeros is not None:
            return self.zeros.insert(val)
        elif char == 0:
            self.zeros = RandomizedSet()
            return self.zeros.insert(val)
        elif self.ones is not None:
            return self.ones.insert(val)
        else:
            self.ones = RandomizedSet()
            return self.ones.insert(val)

    def contains(self, val: int) -> bool:
        """
        Time complexity: O(log(val))
        Space complexity: O(1)
        """
        if not val:
            return self.end

        if val < 0:
            return self.neg is not None and self.neg.contains(-val)

        char = val % 2
        val = val >> 1
        if char == 0:
            return self.zeros is not None and self.zeros.contains(val)
        else:
            return self.ones is not None and self.ones.contains(val)

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.

        Time complexity: O(log(val))
        Space complexity: O(1)
        """
        if not self.contains(val):
            return False

        self.freq -= 1
        if not val:
            self.end = False
            return True

        if val < 0:
            return self.neg.remove(-val)

        char = val % 2
        val = val >> 1
        if char == 0:
            return self.zeros.remove(val)
        else:
            return self.ones.remove(val)

    def getRandom(self) -> int:
        """
        Get a random element from the set.

        Time complexity: O(N), if there are N elements in the structure
        Space complexity: O(1)
        """
        i = random.randint(1, self.freq)
        return self.getElement(i)

    def getElement(self, i: int) -> int:
        """
        Get the ith element.

        We know that there are self.zeros.freq many numbers in the zeros group, self.ones.freq many numbers
        in the ones group, and if there is a zero number

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.neg is not None and i <= self.neg.freq:
            # the last digit is zero
            return -self.neg.getElement(i)

        elif self.zeros is not None and i <= getattr(self.neg, 'freq', 0) + self.zeros.freq:
            return self.zeros.getElement(i - getattr(self.neg, 'freq', 0)) << 1

        elif self.end and i == self.freq:
            # return zero number
            return 0

        else:
            # the digit is 1, but we need to adjust the sequential order
            # to exclude zeros
            i -= getattr(self.neg, 'freq', 0) + getattr(self.zeros, 'freq', 0)
            return (self.ones.getElement(i) << 1) | 1