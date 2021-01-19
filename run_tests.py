"""
quick utils for running tests
"""
from copy import deepcopy
from typing import List, Set


def run_tests(foo, answers: list):
    for args in answers:
        args = list(args)
        corr_ans = args.pop()
        pred_ans = foo(*deepcopy(args))
        assert corr_ans == pred_ans, f'For input {args}, got {pred_ans}, expected {corr_ans}'
    print('All tests passed')


def run_tests_belongs(foo, answers: List or Set):
    """
    check if the output of foo belongs to the list/set of correct answers
    :param foo:
    :param answers:
    :return:
    """
    for args in answers:
        args = list(args)
        corr_ans = args.pop()
        pred_ans = foo(*deepcopy(args))
        assert pred_ans in corr_ans, f'For input {args}, got {pred_ans}, expected answer in {corr_ans}'
    print('All tests passed')