"""
A linked list of length n is given such that each node contains
an additional random pointer, which could point to any node in
the list, or null.

Construct a deep copy of the list. The deep copy should consist
of exactly n brand new nodes, where each new node has its value
set to the value of its corresponding original node. Both the
next and random pointer of the new nodes should point to new
nodes in the copied list such that the pointers in the original
list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list,
where X.random --> Y, then for the corresponding two nodes x and
y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n
nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that
                  the random pointer points to, or null if it does
                  not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.


Constraints:
(*) 0 <= n <= 1000
(*) -10000 <= Node.val <= 10000
(*) Node.random is null or is pointing to some node in the linked list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from LinkedList import ListNode

class Solution:
    def copyRandomList(self, head: 'ListNode') -> 'ListNode':
        converter = {id(None): None}  # key: id of node in head, value: copy of the node
        # copy values and next pointers
        new_head = ListNode(0)
        head_copy = head
        new_head_copy = new_head
        while head_copy is not None:
            new_head_copy.next = ListNode(head_copy.val)
            new_head_copy = new_head_copy.next
            converter[id(head_copy)] = new_head_copy
            head_copy = head_copy.next
        new_head = new_head.next

        # copy random pointers
        head_copy = head
        new_head_copy = new_head
        while head_copy is not None:
            new_head_copy.random = converter[id(head_copy.random)]
            new_head_copy = new_head_copy.next
            head_copy = head_copy.next
        return new_head


if __name__ == '__main__':
    tree_examples = [
        [[7, None],[13,0],[11,4],[10,2],[1,0]],
        [[1,1],[2,1]], [[1,1],[2,1]],
        [[3, None],[None,0],[3, None]],
        []
    ]
    def make_tree(arr):
        head = ListNode('*')
        head2 = head
        mapping = []
        for val, _ in arr:
            head2.next = ListNode(val)
            head2 = head2.next
            mapping.append(head2)
        head = head.next
        head2 = head
        for _, random in arr:
            if random is None:
                head2.random = None
            else:
                head2.random = mapping[random]
            head2 = head2.next
        return head

    tree_examples = [make_tree(arr) for arr in tree_examples]

    print(f'Running tests for copyRandomList')
    for tree in tree_examples:
        copy_tree = Solution().copyRandomList(tree)
        # run checks
        # check that all nodes are copied
        tree_ids = list()
        copy_tree_ids = list()
        tree2 = tree
        while tree2 is not None:
            tree_ids.append(id(tree2))
            tree2 = tree2.next
        copy_tree2 = copy_tree
        while copy_tree2 is not None:
            if id(copy_tree2) in tree_ids:
                print(f'Nodes are not copies for {tree}')
            copy_tree_ids.append(id(copy_tree2))
            copy_tree2 = copy_tree2.next
        # check that values of nodes are identical
        # and check that random pointer points identically for both trees
        tree2 = tree
        copy_tree2 = copy_tree
        while tree2 is not None:
            if copy_tree2 is None:
                print(f'Copied tree is shorter than original tree for {tree}')

            if tree2.val != copy_tree2.val:
                print(f'Non-identical values ({tree2.val}!={copy_tree2.val}) of tree and copied tree for {tree}')

            if tree2.random != copy_tree2.random:
                print(f'Non-identical random indicators ({tree2.random}!={copy_tree2.random}) of tree and copied tree for {tree}')
            tree2 = tree2.next
            copy_tree2 = copy_tree2.next


    print(f'All tests passed.')
