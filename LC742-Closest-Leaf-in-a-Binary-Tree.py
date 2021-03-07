"""
Given a binary tree where every node has a unique value, and a target key k,
find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary
tree to reach any leaf of the tree. Also, a node is called a leaf if it has no
children.

In the following examples, the input tree is represented in flattened form row
by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input:
root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6)
is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""
from TreeNode import TreeNode

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # assign parent
        root.parent = None
        self.assignParent(root)
        # compute distance the closest leaf downwards and the leaf value
        self.distToLeaf(root)

        # find the node with value k
        node = self.getNode(root, k)

        # find the distance to the closest leaf
        closest = node.to_leaf + 1
        leaf_value = node.leaf_value
        node = node.parent
        steps_up = 2
        while node is not None:
            if node.to_leaf + steps_up < closest:
                closest = node.to_leaf + steps_up
                leaf_value = node.leaf_value
            node = node.parent
            steps_up += 1
        return leaf_value

    def distToLeaf(self, root: TreeNode):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if root is None:
            pass
        elif root.left is None and root.right is None:
            root.to_leaf = 1
            root.leaf_value = root.val
        else:
            self.distToLeaf(root.left)
            self.distToLeaf(root.right)
            if getattr(root.left, 'to_leaf', float('inf')) < getattr(root.right, 'to_leaf', float('inf')):
                root.to_leaf = root.left.to_leaf + 1
                root.leaf_value = root.left.leaf_value
            else:
                root.to_leaf = root.right.to_leaf + 1
                root.leaf_value = root.right.leaf_value

    def assignParent(self, root: TreeNode):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if root.left is not None:
            root.left.parent = root
            self.assignParent(root.left)

        if root.right is not None:
            root.right.parent = root
            self.assignParent(root.right)

    def getNode(self, root: TreeNode, k: int) -> TreeNode:
        # find the node with value k
        level = [root, ]
        while level:
            new_level = []
            for node in level:
                if node.val == k:
                    return node

                if node.left is not None:
                    new_level.append(node.left)
                if node.right is not None:
                    new_level.append(node.right)
            level = list(new_level)


if __name__ == '__main__':
    from run_tests import run_tests

    correct_answers = [
        [[1, 3, 2], 1, 2],
        [[1], 1, 1],
        [[1,2,3,4,None,None,None,5,None,6], 2, 3],
        [[1, 2, 3, 4, None, None, None, 5, None, 6], 5, 6],
        [[1, 2, 3, 4, None, None, None, 5, None, 6], 1, 3]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.to_treenode(correct_answers[i][0])
    print(f'Running tests for findClosestLeaf')
    run_tests(Solution().findClosestLeaf, correct_answers)