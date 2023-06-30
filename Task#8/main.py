"""
Task #8
Largest product in a series
Level: Easy
Points: 100
"""
import math


def find_largest_product(t):
    output_array = []

    for _ in range(t):
        size, k = input().strip().split(' ')
        size, k = int(size), int(k)
        n = str(input().strip())
        max_product = -1
        for i in range(size - k + 1):
            actual_number = n[i:i+k]
            product = math.prod([int(x) for x in actual_number])
            if product > max_product:
                max_product = product
        output_array.append(max_product)

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = find_largest_product(t)
print_result(result)
