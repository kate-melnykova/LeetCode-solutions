"""
Given head, the head of a linked list, determine if the linked list
has a cycle in it.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's
next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects
to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects
to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:
(*) The number of the nodes in the list is in the range [0, 104].
(*) -10^5 <= Node.val <= 10^5
(*) pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from LinkedList import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycleWithMemory(self, head: ListNode) -> bool:
        """
        Find if the LinkedList has a cycle by assigning
        visited attribute to it
        :param head:
        :return:
        Runtime complexity: O(n)
        Space complexity: O(n)
        """
        while head is not None:
            if hasattr(head, 'visited'):
                return True
            head.visited = True
            head = head.next
        return False

    def hasCycleNoMemory(self, head) -> bool:
        """
        Find if a LinkedList has a cycle. If it has, then there is n such that
        2^n is greater than the length of the cycle. Therefore, moving along the
        linked list for 2^n steps, we have to meet the original node.

        Increase n until the node is met or until we reach None
        :param head: head of the linked list
        :return: true if the linked list has a cycle, false otherwise

        Runtime complexity: O(n)
        Space complexity: O(1)
        """
        if head is None:
            return False

        n = 1
        memo = id(head)
        head = head.next
        counter = 1 << n - 1
        while head is not None:
            if id(head) == memo:
                return True

            elif counter:
                counter -= 1
            else:
                memo = id(head)
                n += 1
                counter = 1 << n
            head = head.next

        return False


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[3,2,0,-4], 1, True],
        [[1,2], 0, True],
        [[1], -1, False],
        [list(range(100)), 3, True],
        [list(range(100)), -1, False]
    ]
    for i in range(len(correct_answers)):
        arr, pos, ans = correct_answers[i]
        root = ListNode.to_linkedlist(arr)
        if pos == 0:
            node = root
            while node.next is not None:
                node = node.next
            node.next = root
        elif pos > 0:
            node = root
            pos -= 1
            while node.next is not None:
                if not pos:
                    loop_starts = node
                node = node.next
                pos -= 1
            node.next = loop_starts
        correct_answers[i] = [root, ans]

    methods = ['hasCycleWithMemory', 'hasCycleNoMemory', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)
