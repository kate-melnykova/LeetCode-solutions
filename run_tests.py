"""
quick utils for running tests
"""

def run_tests(foo, answers: list):
    for args in answers:
        args = list(args)
        corr_ans = args.pop()
        pred_ans = foo(*args)
        assert corr_ans == pred_ans, f'For input {args}, got {pred_ans}, expected {corr_ans}'
    print('All tests passed')