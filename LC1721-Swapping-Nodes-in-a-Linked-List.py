"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:
Input: head = [1], k = 1
Output: [1]

Example 4:
Input: head = [1,2], k = 1
Output: [2,1]

Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
"""
from LinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        length = self.getLength(head)
        node1 = self.getNode(head, k - 1)
        node2 = self.getNode(head, length - k)
        node1.val, node2.val = node2.val, node1.val
        return head

    def getLength(self, head: ListNode) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def getNode(self, head: ListNode, k: int) -> ListNode:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        for _ in range(k):
            head = head.next
        return head


if __name__ == '__main__':
    import run_tests

    correct_answers = [
        [[1,2,3,4,5], 2, [1,4,3,2,5]],
        [[7,9,6,6,7,8,3,0,9,5], 5, [7,9,6,6,8,7,3,0,9,5]],
        [[1], 1, [1]],
        [[1,2], 2, [2, 1]],
        [[1,2,3], 2, [1,2,3]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = ListNode.to_linkedlist(correct_answers[i][0])
        correct_answers[i][-1] = ListNode.to_linkedlist(correct_answers[i][-1])
    print(f'Running tests for swapNodes')
    run_tests.run_tests(Solution().swapNodes, correct_answers)