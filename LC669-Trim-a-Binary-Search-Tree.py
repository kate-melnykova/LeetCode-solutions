"""
Given the root of a binary search tree and the lowest and highest
boundaries as low and high, trim the tree so that all its elements
lies in [low, high]. Trimming the tree should not change the
relative structure of the elements that will remain in the tree
(i.e., any node's descendant should remain a descendant). It can
be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the
root may change depending on the given bounds.

Example 1.
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Example 3:
Input: root = [1], low = 1, high = 2
Output: [1]

Example 4:
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Example 5:
Input: root = [1,null,2], low = 2, high = 4
Output: [2]


Constraints:
(*) The number of nodes in the tree in the range [1, 10^4].
(*) 0 <= Node.val <= 10^4
(*) The value of each node in the tree is unique.
(*) root is guaranteed to be a valid binary search tree.
(*) 0 <= low <= high <= 10^4
"""
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None

        if root.val < low:
            # we need to exclude the node root
            # note that all values in root.left are less than root.val,
            # so they are less than low
            # exclude all of them, so we need to process root.right only
            return self.trimBST(root.right, low, high)

        elif root.val > high:
            # we need to exclude the node root
            # note that all values in root.right are greater than root.val,
            # so they are greater than high
            # exclude all of them, so we need to process root.left only
            return self.trimBST(root.left, low, high)

        else:
            # we keep root node. Let us processs root.left and root.right
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


if __name__ == '__main__':
    from run_tests import run_tests
    from TreeNode import output_to_list, input_to_treenode

    correct_answers = [
        [[1, 0, 2], 1, 2, [1, None, 2]],
        [[3, 0, 4, None, 2, None, None, 1], 1, 3, [3, 2, None, 1]],
        [[1], 1, 2, [1]],
        [[1, None, 2], 1, 3, [1, None, 2]],
        [[1, None, 2], 2, 4, [2]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
        correct_answers[i][-1] = TreeNode.to_treenode(correct_answers[i][-1])

    methods = ['trimBST', ]
    for method in methods:
        print(f'Running tests for {method}')
        run_tests(getattr(Solution(), method), correct_answers)

