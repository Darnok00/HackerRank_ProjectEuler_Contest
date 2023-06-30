"""
Task #9
Special Pythagorean triplet
Level: Easy
Points: 100
"""
import math


MAX_SIZE = 3000


def find_largest_product(t):
    output_array = []
    pythagorean_triples = []
    for i in range((MAX_SIZE // 3) * 2):
        for j in range(i - 1, 0, -1):
            a_2 = i ** 2 - j ** 2
            a = math.sqrt(a_2)
            if abs(round(a, 0) - a) == 0:
                pythagorean_triples.append([i, j, int(round(a, 0))])
    for _ in range(t):
        n = int(input().strip())
        max_product = -1
        for triple in pythagorean_triples:
            if sum(triple) == n:
                if math.prod(triple) > max_product:
                    max_product = math.prod(triple)

        output_array.append(max_product)

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = find_largest_product(t)
print_result(result)
