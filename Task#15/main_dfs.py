"""
Task #15
Special Pythagorean triplet
Level: Easy
Points: 100
"""


def print_result(result):
    for element in result:
        print(element)


def dfs(x, y, n, m):
    if y == n and x == m:
        return 1

    if y != n and x != m:
        return (dfs(x, y + 1, n, m)) % (10 ** 9 + 7) + (dfs(x + 1, y, n, m)) % (10 ** 9 + 7)
    elif x != m:
        return (dfs(x + 1, y, n, m)) % (10 ** 9 + 7)
    elif y != n:
        return (dfs(x, y + 1, n, m)) % (10 ** 9 + 7)


def find_largest_product(t):
    output_array = []
    for _ in range(t):
        n, m = input().strip().split(' ')
        output_array.append(dfs(0, 0, int(n), int(m)))

    return output_array


t = int(input().strip())
result = find_largest_product(t)
print_result(result)
