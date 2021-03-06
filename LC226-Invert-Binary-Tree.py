"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you
can’t invert a binary tree on a whiteboard so f*** off.
"""
from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Space complexity: O(1) without stack, O(depth) with stack
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[4,2,7,1,3,6,9], [4,7,2,9,6,3,1]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
        correct_answers[i][1] = TreeNode.to_treenode(correct_answers[i][1])

    print(f'Running tests for invertTree')
    run_tests(Solution().invertTree, correct_answers)