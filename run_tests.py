"""
quick utils for running tests
"""
from copy import deepcopy


def run_tests(foo, answers: list):
    for args in answers:
        args = list(args)
        corr_ans = args.pop()
        pred_ans = foo(*deepcopy(args))
        assert corr_ans == pred_ans, f'For input {args}, got {pred_ans}, expected {corr_ans}'
    print('All tests passed')