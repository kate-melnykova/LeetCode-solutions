"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions
(x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each
unique x-coordinate from left to right. Each report is a list of all nodes at a given
x-coordinate. The report should be primarily sorted by y-coordinate from highest
y-coordinate to lowest. If any two nodes have the same y-coordinate in the report,
the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.


Example 1:
Input: root = [3,9,20,null,null,15,7] # in-order traversal
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.


Constraints:
(*) The number of nodes in the tree is in the range [1, 1000].
(*) 0 <= Node.val <= 1000
"""
from typing import List
import bisect

from TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """
        Represent the tree using vertical (y-coord) traversal
        :param root: the root node of the binary tree
        :return: vertical traversal

        Runtime complexity: O(n) (from BFS) + O(width * log(width)),
        where n is the number of nodes, width is the width of three
        Worst case runtime complexity: O(nlog n)

        Space complexity: O(n)
        """
        if root is None:
            return []

        # we do modified BFS, we add and pop nodes from the array nodes
        level = [(root, 0), ]  # entries of nodes: (node, y-coordinate)
        # preliminary, make dictionary of key=y-coordinate,
        # value=list of all values of nodes who have given y-coordinate
        ans = dict()
        while level:
            level_new = list()
            new_ans = dict()
            for node, y in level:
                # add it to ans
                if y not in new_ans:
                    new_ans[y] = []
                bisect.insort(new_ans[y], node.val)
                # add node.left to level
                if node.left is not None:
                    level_new.append((node.left, y - 1))
                # add node.right to level
                if node.right is not None:
                    level_new.append((node.right, y + 1))
            level = list(level_new)
            for y, vals in new_ans.items():
                ans[y] = ans.get(y, []) + vals

        # flatten the list of lists
        return [ans[y] for y in sorted(ans)]


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[3,9,20,None,None,15,7], [[9],[3,15],[20],[7]]],
        [[1,2,3,4,5,6,7], [[4],[2],[1,5,6],[3],[7]]],
        [[10, 2, 3, 4, 5, 6, 7], [[4], [2], [10, 5, 6], [3], [7]]],
    ]

    print(f'Running tests for verticalTraversal')

    def solution_method(node_list: List[int or None]) -> List[List[int]]:
        node = TreeNode.to_treenode(node_list)
        return Solution().verticalTraversal(node)
    run_tests(solution_method, correct_answers)