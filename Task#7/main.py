"""
Task #7
10001st prime
Level: Easy
Points: 100
"""
# This constant is determined experimentally,
# in order to find the optimal sieve size that will return at least 10^4 prime numbers
SIZE_SIEVE = 110000


def prime_eratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [i for i, n in enumerate(prime) if n][2:]


def find_prime(t):
    output_array = []
    primes = prime_eratosthenes(SIZE_SIEVE)

    for _ in range(t):
        n = int(input().strip())
        output_array.append(primes[n-1])

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = find_prime(t)
print_result(result)
