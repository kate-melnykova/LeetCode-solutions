"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from typing import List

from TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        List all nodes from the binary tree that can be "seen" from the right side
        :param root: the root node of the binary tree
        :return: list of node values

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if root is None:
            return []

        ans = list()
        level = [root, ]
        while level:
            ans.append(level[-1].val)
            new_level = list()
            for node in level:
                if node.left is not None:
                    new_level.append(node.left)
                if node.right is not None:
                    new_level.append(node.right)
            level = list(new_level)
        return ans


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1,2,3,None,5,None,4], [1,3,4]],
        [[1,2,3,None,5,None,4,6, 7, None, None, None, 8], [1, 3, 4, 7, 8]],
        [None, []],
        [[1,None,2, None,3, None, 4], [1,2,3,4]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])

    print(f'Running tests for rightSideView')
    run_tests(Solution().rightSideView, correct_answers)