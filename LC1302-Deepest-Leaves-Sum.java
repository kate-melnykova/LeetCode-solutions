/*
Given the root of a binary tree, return the sum of values
of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 100
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int deepestLeavesSum(TreeNode root) {
        int[] data = deepestLeavesSumHelper(root);
        return data[0];
    }

    private int[] deepestLeavesSumHelper(TreeNode root){
        // returns {nodesSum, depth of tree}
        if (root == null)
            return new int[]{0, 0};
        if ((root.left == null) && (root.right == null)){
            return new int[]{root.val, 1};
        }
        int[] leftTree = deepestLeavesSumHelper(root.left);
        int[] rightTree = deepestLeavesSumHelper(root.right);
        if (leftTree[1] == rightTree[1]){
            return new int[]{leftTree[0] + rightTree[0], leftTree[1] + 1};
        } else if (leftTree[1] < rightTree[1]){
            rightTree[1]++;
            return rightTree;
        } else {
            leftTree[1]++;
            return leftTree;
        }
    }
}