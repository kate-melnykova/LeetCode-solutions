"""
Given the root of a binary tree, return the sum of values
of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:
(*) The number of nodes in the tree is in the range [1, 10^4].
(*) 1 <= Node.val <= 100
"""
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level_new = [root, ]
        while level_new:
            level = list(level_new)
            level_new = list()
            for node in level:
                if node.left is not None:
                    level_new.append(node.left)
                if node.right is not None:
                    level_new.append(node.right)
        return sum(node.val for node in level)


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [[1,2,3,4,5,None,6,7,None,None,None,None,8], 15],
        [[6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], 19]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
    print(f"Running tests for deepestLeavesSum")
    run_tests.run_tests(Solution().deepestLeavesSum, correct_answers)