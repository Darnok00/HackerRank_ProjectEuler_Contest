"""
Task #3
Largest prime factor
Level: Easy
Points: 100
"""


def print_result(result):
    for element in result:
        print(element)


def decompose_prime_factors(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())

        largest_fac = -1
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                while n % i == 0:
                    n //= i
                largest_fac = max(largest_fac, i)

        largest_fac = max(largest_fac, n)
        output_array.append(largest_fac)

    return output_array


t = int(input().strip())
result = decompose_prime_factors(t)
print_result(result)
