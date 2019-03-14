from test_framework import generic_test


def parity(x):
    # Method 1: Brute force
    # result = 0
    # while x:
    #     result ^= x & 1
    #     x >> 1
    # return result

    # Method 2: Slightly faster version of brute force by dropping the least set bit
    # O(k) where k is the number of bits set to 1
    # result = 0
    # while x:
    #     result ^= 1
    #     x &= x-1
    # return result

    # Method 3: cache and abuse XOR property of being associative
    # Assume working with 8-bit word
    # x =^ x >> 32
    # x =^ x >> 16
    # x =^ x >> 8
    # x =^ x >> 4
    # x =^ x >> 2
    # x =^ x >> 1
    # return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
