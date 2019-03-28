from test_framework import generic_test
import math
# least significant bit: n & 1
# most significant bit: ??


def most_significant_bit_inefficient(x):
    mst = 0
    while x > 0:
        x >>= 1
        mst += 1
    return mst

# Fast way to get most and least sig bit
# The number of digits, n, in the input's string representation is the log (base 10)
# of the input value, x. n = math.floor(math.log(x)) + 1
# LSB: x mod 10, MSB: x / 10**(n-1)


def is_palindrome_number(x):
    # Efficient
    # O(n) time, O(1) space
    if x <= 0:
        return x == 0

    
    num_digits = math.floor(math.log10(x)) + 1 # Gets the length of the number's string representation
    msd_mask = 10**(num_digits-1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask # Remove most significant digit of x
        x //= 10 # Remove least significant digit of x
        msd_mask //= 100 # Chop the mask down by 100 cuz we lost a digit on both ends
    
    return True



    # BRUTE FORCE
    # O(n) space and time complexity
    # n = str(x)
    # arr = [c for c in n]
    # return arr == list(reversed(arr))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
