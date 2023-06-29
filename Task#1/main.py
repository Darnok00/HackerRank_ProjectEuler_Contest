"""
Task #1
Multiple 3 and 5
Level: Easy
Points: 100
"""


def sum_arithmetic_seq(n, a1, r):
    return (n * (2 * a1 + (n - 1) * r)) // 2


def multiple3and5(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())
        multiple_threes = (n - 1) // 3
        multiple_fives = (n - 1) // 5
        multiple_fifteens = (n - 1) // 15
        # sum arithmetic sequence
        sum_multiple_threes = sum_arithmetic_seq(multiple_threes, 3, 3)
        sum_multiple_fives = sum_arithmetic_seq(multiple_fives, 5, 5)
        sum_multiple_fifteens = sum_arithmetic_seq(multiple_fifteens, 15, 15)
        # sum multiple threes and fives minus common part
        result = sum_multiple_fives + sum_multiple_threes - sum_multiple_fifteens
        output_array.append(result)

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = multiple3and5(t)
print_result(result)
