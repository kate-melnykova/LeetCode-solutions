from typing import List
from functools import wraps


class IncorrectTreeNodeTranscription(Exception):
    pass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self) -> List[int or str]:
        level = [self, ]
        lst = []
        while level:
            new_level = list()
            for node in level:
                if node is None:
                    lst.append(None)
                else:
                    lst.append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
            level = list(new_level)

        return lst

    @classmethod
    def to_treenode(cls, arr: List[int or str] or None) -> 'TreeNode' or None:
        if not arr or arr[0] is None:
            return None

        level = [TreeNode(arr.pop(0)), ]
        root = level[0]
        while level:
            new_level = []
            for node in level:
                if not arr:
                    break
                elif arr[0] is None:
                    arr.pop(0)
                else:
                    node.left = TreeNode(arr.pop(0))
                    new_level.append(node.left)

                if not arr:
                    break
                elif arr[0] is None:
                    arr.pop(0)
                else:
                    node.right = TreeNode(arr.pop(0))
                    new_level.append(node.right)
            level = list(new_level)
        return root

    def __repr__(self):
        return str(self.to_list())

    def __eq__(self, other):
        this = self
        if this is None and other is None:
            return True

        if this is None or other is None:
            return False

        if this.val != other.val:
            return False

        return self.left == other.left and self.right == other.right


def input_to_treenode(foo, args_idx=[], kwargs_keys=[]):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        nonlocal args_idx, kwargs_keys
        if not args_idx and not kwargs_keys:
            args_idx = list(range(len(args)))
            kwargs_keys = list(kwargs.keys())

        args = list(args)
        print(args)
        for idx in args_idx:
            print(idx)
            args[idx] = TreeNode.to_treenode(args[idx])
        for key in kwargs:
            kwargs[key] = TreeNode.to_treenode(kwargs[key])
        return foo(*args, **kwargs)
    return wrapper


def output_to_list(foo, output_idx=[]):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        output = foo(*args, **kwargs)
        if isinstance(output, TreeNode):
            return output.to_list()

        nonlocal output_idx
        if not output_idx:
            output_idx = list(range(len(output)))

        type = type(output)
        output = list(output)
        for idx in output_idx:
            print(idx)
            output[idx] = output[idx].to_list()
        return type(output)
    return wrapper


if __name__ == '__main__':
    lists = [
        [1, None, None],
        [1, 2, None, None, 3, None, None],
        [1,None,2,None,3, None, None],
        [1, 4, None, None, 3, None, None],
        [3,9,20,None,None, 15, 7]
    ]
    for lst in lists:
        lst2 = TreeNode.to_treenode(list(lst)).to_list()
        assert lst2 == lst + [None, ] * (len(lst2) - len(lst)), str(lst)