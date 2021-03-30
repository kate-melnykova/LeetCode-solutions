"""
You are given the root of a binary tree with n nodes,
where each node is uniquely assigned a value from 1 to n.
You are also given a sequence of n values voyage, which
is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping
its left and right subtrees. For example, flipping node
1 will have the following effect:
       1                    1
      / \                  / \
    2    3                3   2

Flip the smallest number of nodes so that the pre-order
traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may
return the answer in any order. If it is impossible to flip
the nodes in the tree to make the pre-order traversal match
voyage, return the list [-1].



Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that
the pre-order traversal matches voyage.

Example 2:
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the
pre-order traversal matches voyage.

Example 3:
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches
voyage, so no nodes need to be flipped.


Constraints:
(*) The number of nodes in the tree is n.
(*) n == voyage.length
(*) 1 <= n <= 100
(*) 1 <= Node.val, voyage[i] <= n
(*) All the values in the tree are unique.
(*) All the values in voyage are unique.
"""
from typing import List

import TreeNode


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.voyage = voyage
        ans, i = self._flipMatchVoyage(root, 0)
        if ans is None:
            return [-1, ]
        else:
            return ans

    def _flipMatchVoyage(self, root: TreeNode, i: int) -> List[List[int] or None or int]:
        if root is None:
            return [[], i]

        # check the value of the root node matches the first entry in voyage
        if len(self.voyage) == i or root.val != self.voyage[i]:
            return [None, i]

        i += 1
        # check if the twist is needed
        # first, verify that it is not a leaf node
        if root.left is None and root.right is None:
            return [[], i]

        # if the left child is None, no flipping required
        if root.left is None:
            return self._flipMatchVoyage(root.right, i)

        # this is not the leaf node, so self.voyage[i] should match either root.left.val or root.right.val
        if root.left is not None and root.left.val == self.voyage[i]:
            # no need to twist trees
            left_twists, i = self._flipMatchVoyage(root.left, i)
            if left_twists is None:
                return [None, i]

            right_twists, i = self._flipMatchVoyage(root.right, i)
            if right_twists is None:
                return [None, i]

            return [left_twists + right_twists, i]

        if root.right is not None and root.right.val == self.voyage[i]:
            # twist trees
            left_twists, i = self._flipMatchVoyage(root.right, i)
            if left_twists is None:
                return [None, i]

            right_twists, i = self._flipMatchVoyage(root.left, i)
            if right_twists is None:
                return [None, i]

            return [[root.val, ] + left_twists + right_twists, i]

        return [None, i]


if __name__ == "__main__":
    import run_tests

    correct_answers = [
        [[1, 2], [2, 1], [-1, ]],
        [[1, 2, 3], [1, 3, 2], [1, ]],
        [[1, 2, 3], [1, 2, 3], []],
        [[1, 2, 3, 4, 5], [1, 3, 2, 4, 5], [1, ]],
        [[1, 2, 3, 4, 5], [1, 2, 3, 5, 4], [-1]],
        [[1, 2, 3, 4, 5, 6, 7], [1, 3, 6, 7, 2, 5, 4], [1, 2]],
        [[1, None, 2], [1, 2], []]
    ]
    for i in range(len(correct_answers)):
        correct_answers[i][0] = TreeNode.TreeNode.to_treenode(correct_answers[i][0])
    print(f"Running tests for flipMatchVoyage")
    run_tests.run_tests(Solution().flipMatchVoyage, correct_answers)
