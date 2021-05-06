/*
Given the head of a singly linked list where elements are sorted in ascending
order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents
the shown height balanced BST.

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [0]
Output: [0]

Example 4:
Input: head = [1,3]
Output: [3,1]


Constraints:
The number of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5
*/
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
         if (head == null){
             return null;
         }
        ListNode head2 = head;
        int length = 0;
        while (head2 != null){
            length++;
            head2 = head2.next;
        }
        return sortedListToBSTHelper(head, length);
    }

    private TreeNode sortedListToBSTHelper(ListNode head, int length){
        if (length == 0){
            return null;
        } else if (length == 1){
            return new TreeNode(head.val);
        }
        // find mid-node and make it a head
        int mid_length = length / 2;
        ListNode temp = head;
        for (int i = 0; i < mid_length - 1; i++){
            temp = temp.next;
        }
        // split LinkedList into two
        ListNode rightTree = temp.next;
        temp.next = null;

        TreeNode root = new TreeNode(rightTree.val);
        rightTree = rightTree.next;
        root.left = sortedListToBSTHelper(head, mid_length);
        root.right = sortedListToBSTHelper(rightTree, length - 1 - mid_length);
        return root;
    }
}