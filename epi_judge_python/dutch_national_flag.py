import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # solution 1 - my solution
    # O(n) space, O(n) time
    # pivot = A[pivot_index]
    # less, equal, greater = [],[],[]
    # for el in A:
    #     if el < pivot:
    #         less.append(el)
    #     elif el == pivot:
    #         equal.append(el)
    #     else:
    #         greater.append(el)
    # a = less + equal + greater
    # for i in range(len(A)):
    #     A[i] = a[i]

    # solution 2
    # O(1) space, O(n^2) time
    # pivot = A[pivot_index]
    # for i in range(len(A)):
    #     for j in range(i + 1, len(A)):
    #         if A[j] < pivot:
    #             A[i], A[j] = A[j], A[i]
    #             break
    # for i in reversed(range(len(A))):
    #     for j in reversed(range(i)):
    #         if A[j] > pivot:
    #             A[i], A[j] = A[j], A[i]
    #             break

    # Solution 3
    # O(1) space, O(n) time
    # pivot = A[pivot_index]
    # smaller = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[smaller] = A[smaller], A[i]
    #         smaller += 1

    # larger = len(A)-1
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot:
    #         A[i], A[larger] = A[larger], A[i]
    #         larger -= 1

    # Solution 4
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]

    # Lesson: Use pointers to track


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
