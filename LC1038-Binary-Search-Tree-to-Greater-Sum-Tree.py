"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key
of the original BST is changed to the original key plus sum of all keys greater than the
original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Example 3:
Input: root = [1,0,2]
Output: [3,3,2]

Example 4:
Input: root = [3,2,4,1]
Output: [7,9,4,10]

Constraints:
(*) The number of nodes in the tree is in the range [0, 10^4].
(*) -10^4 <= Node.val <= 10^4
(*) All the values in the tree are unique.
(*) root is guaranteed to be a valid binary search tree.
"""
from TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode, greater_sum: int = 0, total_sum: int = 0) -> TreeNode:
        """
        Convert BST to greater sum tree with O(1) space

        Time complexity: O(n)
        Space complexity: O(1)

        Note that if we have O(n) space, than we can find the BST by traversing to tree in-order and
        accumulating the sum.
        """
        if root is None:
            return None

        if root.right is not None:
            self.convertBST(root.right, greater_sum)
            greater_sum = root.right.val
            node = root.right
            while node is not None:
                greater_sum = node.val
                node = node.left

        root.val += greater_sum
        self.convertBST(root.left, root.val)
        return root


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8],
         [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]],
        [[0,None,1], [1,None,1]],
        [[1,0,2], [3,3,2]],
        [[3,2,4,1], [7,9,4,10]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
        correct_answers[i][1] = TreeNode.to_treenode(correct_answers[i][1])
    print(f'Running tests for convertBST')
    run_tests(Solution().convertBST, correct_answers)

