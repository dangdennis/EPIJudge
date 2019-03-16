import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
    curr_even, curr_odd = 0, len(A) - 1
    while curr_even < curr_odd:
        if A[curr_even] % 2 == 0:
            curr_even += 1
        # If instead we find an odd, just repetitively swap 
        # with the other end until we get an even
        else:
            A[curr_even], A[curr_odd] = A[curr_odd], A[curr_even]
            curr_odd -= 1
    return A


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_array.py",
                                       'even_odd_array.tsv', even_odd_wrapper))
