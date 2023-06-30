"""""
Task #10
Summation of primes
Level: Medium
Points: 100
"""


SIZE = 1000000


def print_result(result):
    for element in result:
        print(element)


def prime_eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime


def find_sum_primes(t):
    output_array = []
    primes = prime_eratosthenes(SIZE)
    dict_sum = {}
    act_sum = 0

    for i in range(2, SIZE):
        if primes[i]:
            act_sum += i
        dict_sum[i] = act_sum

    for _ in range(t):
        n = int(input().strip())
        sum_primes = dict_sum[n]
        output_array.append(sum_primes)

    return output_array


t = int(input().strip())
result = find_sum_primes(t)
print_result(result)