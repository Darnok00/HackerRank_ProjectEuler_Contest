"""
Task #6
Sum square difference
Level: Easy
Points: 100
"""


def find_difference(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())
        square_sum = (((1 + n) * n) // 2) ** 2
        sum_squares = sum([x ** 2 for x in range(n + 1)])
        output_array.append(abs(sum_squares - square_sum))

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = find_difference(t)
print_result(result)
