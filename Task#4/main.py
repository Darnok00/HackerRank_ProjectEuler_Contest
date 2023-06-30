"""
Task #4
Largest palindrome product
Level: Medium
Points: 100
"""


def print_result(result):
    for element in result:
        print(element)


def generate_palindromes(boundary):
    palindromes = []

    for i in range(100, (boundary // 1000) + 1):
        palindrome = (i * 1000 + ((i % 10) * 100) + ((i // 10) % 10) * 10 + (i // 100))
        if palindrome < boundary:
            palindromes.append(palindrome)

    return palindromes


def is_3numbers_products(n):
    for i in range (100, int(n ** (1/2)) + 1):
        if n % i == 0 and len(str(n // i)) == 3:
            return True
    return False


def find_largest_product(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())
        palindromes = (generate_palindromes(n))
        palindromes.reverse()
        for palindrome in palindromes:
            if is_3numbers_products(palindrome):
                output_array.append(palindrome)
                break

    return output_array


t = int(input().strip())
result = find_largest_product(t)
print_result(result)
