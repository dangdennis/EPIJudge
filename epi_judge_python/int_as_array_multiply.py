from test_framework import generic_test


def multiply(num1, num2):
    sign = 1
    if num1[0] < 0 and num2[0] < 0:
        sign = 1
    elif num1[0] < 0 or num2[0] < 0:
        sign = -1

    result = [0] * (len(num1) + len(num2))
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            # increase by i to move the starting point to the left as we multiply
            # += to keep running total
            result[i + j + 1] += num2[j] * num1[i]
            result[i + j] += result[i + j + 1] // 10  # carry over
            result[i + j + 1] %= 10  # keep remainder

    # Trim the non-zeroes in the front
    print(result)
    for i in range(len(result)):
        if result[i] > 0:
            result = result[i:]
            break
    
    print(result)
    return [sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
