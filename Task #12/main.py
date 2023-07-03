"""""
Task #12
Highly divisible triangular number
Level: Easy
Points: 100
Python is too slow so i converted my code for cpp to get 100 points
"""
MAX_N = 1000


def print_result(result):
    for element in result:
        print(element)


def get_number_dividers(n):
    number_dividers = 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            number_dividers += 2
            if i * i == n:
                number_dividers -= 1

    return number_dividers


def get_triangle_dividers_dict(max_n):
    dict_triangle_dividers = {}
    actual_triangle, number_triangle, max_dividers = 1, 1, 1

    while max_dividers < max_n:
        number_triangle += 1
        actual_triangle += number_triangle
        number_dividers = get_number_dividers(actual_triangle)
        if number_dividers > max_dividers:
            for i in range(max_dividers, number_dividers):
                dict_triangle_dividers[i] = actual_triangle
            max_dividers = number_dividers

    return dict_triangle_dividers


def find_triangles(t):
    output_array = []
    dict_triangles_dividers = get_triangle_dividers_dict(MAX_N)

    for _ in range(t):
        n = int(input().strip())
        output_array.append(dict_triangles_dividers[n])

    return output_array


t = int(input().strip())
result = find_triangles(t)
print_result(result)
