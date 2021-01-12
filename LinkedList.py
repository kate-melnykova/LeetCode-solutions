"""
LinkedList functional
"""
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        lst = []
        head = self
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst

    @staticmethod
    def to_linkedlist(arr: List[int]):
        head = ListNode('*')
        memo = head
        for n in arr:
            head.next = ListNode(n)
            head = head.next
        return memo.next

    def __eq__(self, other):
        this = self
        while this is not None and other is not None:
            if this.val != other.val:
                return False

            this = this.next
            other = other.next
        return this is None and other is None

    def __repr__(self):
        return f'{self.to_list()}'