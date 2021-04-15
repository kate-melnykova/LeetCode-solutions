"""
Given the head of a linked list and a value x, partition
it such that all nodes less than x come before nodes
greater than or equal to x.

You should preserve the original relative order of the
nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

from LinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Runtime complexity: O(n)
        Space complexity: O(1)
        """
        node = ListNode("*")
        node.next = head
        memo = node
        head_fast = node
        while head_fast.next is not None and head_fast.next.val < x:
            head_fast = head_fast.next
        head_slow = head_fast
        while head_fast.next is not None:
            if head_fast.next.val < x:
                node = self.remove_node(head_fast)
                self.insert_node(head_slow, node)
                head_slow = head_slow.next
            else:
                head_fast = head_fast.next
        return memo.next

    def remove_node(self, head: ListNode) -> ListNode:
        """
        Runtime and space complexity: O(1)
        """
        node = head.next
        head.next = head.next.next
        node.next = None
        return node

    def insert_node(self, head: ListNode, node: ListNode) -> None:
        """
        Runtime and space complexity: O(1)
        """
        node.next = head.next
        head.next = node


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [[1,4,3,2,5,2], 3, [1,2,2,4,3,5]],
        [[2,1], 2, [1,2]]
    ]

    for i in range(len(correct_answers)):
        correct_answers[i][0] = ListNode.to_linkedlist(correct_answers[i][0])
        correct_answers[i][-1] = ListNode.to_linkedlist(correct_answers[i][-1])
    print(f"Running tests for partition")
    run_tests.run_tests(Solution().partition, correct_answers)