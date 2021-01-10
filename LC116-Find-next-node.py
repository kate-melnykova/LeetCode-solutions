import typing


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        find the next node for each node with O(1) given space
        :param root: root of the tree
        :return: root of the tree with the next attribute assigned
        Runtime: O(n2^n) where n is the depth of tree
        Worst case: O(m2^m), where m is the number of nodes
        Best case: O^(log(m)2^(log(m)) = O(mlog(m)) holds for the balanced tree

        Space complexity: O(1)
        """
        level = -1
        is_next_level = True
        while is_next_level:
            level += 1
            node_id = 1 << level
            is_next_level = False
            prev = None
            while node_id < (1 << (level + 1)):
                # check if the node with the given instruction exists
                instruction = str(bin(node_id))[3:]
                node = root
                node_exists = True
                for direction in instruction:
                    if node is None:
                        node_exists = False
                        break

                    elif direction == '0':
                        node = node.left
                    else:
                        node = node.right
                if node_exists and prev is not None:
                    prev.next = node
                    prev = node
                    prev.next = None  # if prev does not have next attribute, assign it here
                elif node_exists:
                    prev = node
                    prev.next = None  # just in case, assign this attribute

                if node_exists and (node.left is not None or node.right is not None):
                    is_next_level = True

                node_id += 1
        return root