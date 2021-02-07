"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
(*) The number of nodes in the tree is in the range [1, 5000].
(*) 1 <= Node.val <= 10^7
(*) root is a binary search tree.
(*) 1 <= val <= 10^7
"""
from TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Find the node with the given value in the binary search tree
        :param root: the root of the BST
        :param val: value to be found in the BST
        :return: the node if it exists in the BST else None

        Time complexity: worst case O(n),
                        O(log n) if tree is balanced
        Space complexity: O(1)
        """
        if root is None or root.val == val:
            return root

        elif root.val < val:
            return self.searchBST(root.right, val)

        else:
            return self.searchBST(root.left, val)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[4,2,7,1,3], 2, [2,1,3]],
        [[4,2,7,1,3], 5, []]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
        correct_answers[i][-1] = TreeNode.to_treenode(correct_answers[i][-1])

    print(f'Run tests for searchBST')
    run_tests(Solution().searchBST, correct_answers)