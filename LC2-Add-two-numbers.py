"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from LinkedList import ListNode
from run_tests import run_tests


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        over = 0
        head = ListNode('*')
        ans = head
        while l1 is not None and l2 is not None:
            sum_ = l1.val + l2.val + over
            if sum_ > 9:
                over = 1
                ans.next = ListNode(sum_ - 10)
            else:
                over = 0
                ans.next = ListNode(sum_)
            l1 = l1.next
            l2 = l2.next
            ans = ans.next

        while l1 is not None:
            sum_ = l1.val + over
            if sum_ < 10:
                ans.next = ListNode(sum_)
                over = 0
            else:
                ans.next = ListNode(0)
            ans = ans.next
            l1 = l1.next

        while l2 is not None:
            sum_ = l2.val + over
            if sum_ < 10:
                ans.next = ListNode(sum_)
                over = 0
            else:
                ans.next = ListNode(0)
                over = 1
            ans = ans.next
            l2 = l2.next

        if over:
            ans.next = ListNode(1)

        return head.next


if __name__ == "__main__":
    corr_answers = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
    ]
    corr_answers = [[ListNode.to_linkedlist(l) for l in args] for args in corr_answers]
    run_tests(Solution().addTwoNumbers, corr_answers)