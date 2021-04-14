"""
You are given a nested list of integers nestedList. Each element is either
an integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested
list and false otherwise.


Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order
of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order
of elements returned by next should be: [1,4,6].


Constraints:
(*) 1 <= nestedList.length <= 500
(*) The values of the integers in the nested list is in the range [-10^6, 10^6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from typing import List

class NestedInteger:
    def __init__(self, entry):
        if isinstance(entry, int):
            self._integer = entry
            self._list = None
        else:
            self._integer = None
            self._list = entry

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self._integer, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._integer

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self._list


class NestedIterator:
    def __init__(self, nestedList: List["NestedInteger"]):
        self.nestedList = nestedList
        self.current_lst = []
        self.next_item = None

    def next(self) -> int:
        if not self.hasNext():
            raise

        ans = self.next_item
        self.next_item = None
        return ans

    def hasNext(self) -> bool:
        if self.next_item is not None:
            return True

        while self.current_lst:
            item = self.current_lst.pop(0)
            if isinstance(item, int):
                self.next_item = item
                return True

            # it is a nestedInteger
            n = item.getInteger()
            if n is not None:
                self.next_item = n
                return True

            lst = item.getList()
            self.current_lst = lst + self.current_lst

        if self.nestedList:
            nested_lst = self.nestedList.pop(0)
            n = nested_lst.getInteger()
            if n is not None:
                self.next_item = n
                return True

            self.current_lst = nested_lst.getList()
            return self.hasNext()

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())