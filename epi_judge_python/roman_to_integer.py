from test_framework import generic_test
import functools


def roman_to_integer(s):
    T = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # EIP solution
    # return functools.reduce(
    #     # Add the val else if the current letter is less than the next, we'll substract instead
    #     # i.e IX = 9
    #     lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
    #     # We'll iterate backwards
    #     reversed(range(len(s) - 1)),
    #     T[s[-1]]
    # )

    num = 0

    print('STRING:', s)

    for i in range(len(s)-1,-1, -1):
        if i > 0 and T[s[i-1]] < T[s[i]]:
            num += -T[s[i]]
        else:
            num += T[s[i]]

    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
