"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every
node differ in height by no more than 1.

Example 1.
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2.
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
(*) The number of nodes in the tree is in the range [0, 5000].
(*)-10^4 <= Node.val <= 10^4
"""
from TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Checking isBalanced using new depth attribute
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if root is None: return True
        
        if root.left is not None:
            is_left_balanced = self.isBalanced(root.left)
            left_depth = root.left.depth
        else:
            is_left_balanced = True
            left_depth = 0
            
        if root.right is not None:
            is_right_balanced = self.isBalanced(root.right)
            right_depth = root.right.depth
        else:
            is_right_balanced = True
            right_depth = 0
        
        # determine the depth
        root.depth = max(right_depth, left_depth) + 1
        
        # determine if the node is balanced
        root.is_balanced = is_left_balanced and is_right_balanced and abs(right_depth - left_depth) <= 1
        return root.is_balanced


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[3, 9, 20, None, None, 15, 7], True],
        [[1,2,2,3,3,None,None,4,4], False],
        [[], True]
    ]
    correct_answers = [
        [TreeNode.to_treenode(lst), ans] for lst, ans in correct_answers
    ]
    print('Run tests for isBalanced')
    run_tests(Solution().isBalanced, correct_answers)