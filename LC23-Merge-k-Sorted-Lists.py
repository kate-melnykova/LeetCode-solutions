"""
You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
(*) k == lists.length
(*) 0 <= k <= 10^4
(*) 0 <= lists[i].length <= 500
(*) -10^4 <= lists[i][j] <= 10^4
(*) lists[i] is sorted in ascending order.
(*) The sum of lists[i].length won't exceed 10^4.
"""
from typing import List
import bisect
from functools import partial

from LinkedList import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged = ListNode('*')
        merged_head = merged
        first_nodes_vals = list()
        for i, node in enumerate(lists):
            if node is not None:
                bisect.insort(first_nodes_vals, (node.val, i))

        while first_nodes_vals:
            # find the node with the next min value
            _, idx = first_nodes_vals.pop(0)
            # add it to the merged seq
            merged.next = lists[idx]
            # update merged and lists[idx]
            new_head_subseq = lists[idx].next
            merged = merged.next
            merged.next = None
            lists[idx] = new_head_subseq
            # add new value to first_nodes_vals if applicable
            if lists[idx] is not None:
                bisect.insort(first_nodes_vals, (lists[idx].val, idx))
        return merged_head.next


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]],
        [[], []],
        [[[]], []],
    ]

    def solve_for_lists(lst: List[List[int]]) -> 'ListNode':
        lst = [ListNode.to_linkedlist(l) for l in lst]
        ans = Solution().mergeKLists(lst)
        if ans is None:
            return []
        else:
            return ans.to_list()

    print(f'Running tests for mergeKLists')
    run_tests(solve_for_lists, correct_answers)
