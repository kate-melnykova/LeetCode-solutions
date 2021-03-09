"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""
from TreeNode import TreeNode


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        elif d == 2:
            return self.injectNode(root, v)

        else:
            if root.left is not None:
                self.addOneRow(root.left, v, d - 1)
            if root.right is not None:
                self.addOneRow(root.right, v, d - 1)
            return root

    def injectNode(self, root: TreeNode, v: int) -> TreeNode:
        node1 = TreeNode(v)
        node1.left = root.left
        node2 = TreeNode(v)
        node2.right = root.right
        root.left = node1
        root.right = node2
        return root


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[4, 2, 6, 3, 1, 5], 1, 1, [1,4, None,2,6,3,1,5]],
        [[4,2,6,3,1,5],1,2, [4,1,1,2,None,None,6,3,1,5]],
        [[4, 2, 6, 3, 1, 5], 1, 3, [4,2,6,1,1,1,1,3,None,None,1,5]],
        [[4, 2, 6, 3, 1, 5], 1, 4, [4,2,6,3,1,5,None,1,1,1,1,1,1]]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
        correct_answers[i][-1] = TreeNode.to_treenode(correct_answers[i][-1])

    print(f'Running tests for addOneRow')
    run_tests(Solution().addOneRow, correct_answers)