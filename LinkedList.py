"""
LinkedList functional
"""
from typing import List
from functools import wraps


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        lst = []
        head = self
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst

    @staticmethod
    def to_linkedlist(arr: List[int]):
        head = ListNode('*')
        memo = head
        for n in arr:
            head.next = ListNode(n)
            head = head.next
        return memo.next

    def __eq__(self, other):
        this = self
        while this is not None and other is not None:
            if this.val != other.val:
                return False

            this = this.next
            other = other.next
        return this is None and other is None

    def __repr__(self):
        return f'{self.to_list()}'

"""
def input_to_linked_list(*args, **kwargs):
    def inner(foo, args_idx=[], kwargs_keys: List[int] = []):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            args = list(args)
            if not args_idx and not kwargs_keys:
                args_idx = list(range(len(args)))
                kwargs_keys = list(kwargs.keys())
            for idx in args_idx:
                args[idx] = ListNode.to_linkedlist(args[idx])
            for key in kwargs_keys:
                kwargs[key] = ListNode.to_linkedlist(kwargs[key])
        return foo(*args, **kwargs)
    return wrapper


def output_from_linked_list(foo, output_idx=[]):
    @wraps(foo)
    def wrapped(*args, **kwargs):
        output = foo(*args, **kwargs)
        if not isinstance(output, list) and not isinstance(output, tuple):
            return ListNode.to_list(output)

        if not output_idx:
            output_idx = list(range(len(output)))
        output = list(output)
        for idx in output_idx:
            output[idx] = ListNode.to_linkedlist(output[idx])
        return output
    return wrapped


def inp_to_LN_outp_from_LN(foo, args_idx: List[int] = [], kwargs_keys: List[int] = [], output_idx: List[int] = []):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        decorated = output_from_linked_list(input_to_linked_list(foo,
                                                           args_idx=args_idx,
                                                           kwargs_keys=kwargs_keys),
                                      output_idx=output_idx)
        return decorated(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @input_to_linked_list
    def sum_of_node_vals(node: 'ListNode') -> int:
        sum_ = 0
        while node is not None:
            sum_ += node.val
            node = node.next
        return sum_
    assert sum_of_node_vals([1, 2, 3]) == 6
"""