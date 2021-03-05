"""
Given a non-empty binary tree, return the average value of the nodes on
each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on
level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        ave = []

        level = [root, ]
        while level:
            new_level = []
            average = 0
            for node in level:
                average += node.val
                if node.left is not None:
                    new_level.append(node.left)
                if node.right is not None:
                    new_level.append(node.right)
            ave.append(average / len(level))
            level = list(new_level)
        return ave


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[3,9,20,15,7], [3.0, 14.5, 11.0]],
        [[3,9,20,15,7,None, None,2], [3.0, 14.5, 11.0, 2.0]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
    print(f'Running tests for averageOfLevels')
    run_tests(Solution().averageOfLevels, correct_answers)