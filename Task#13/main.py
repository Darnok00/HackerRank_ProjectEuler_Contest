"""""
Task#13
Large sum
Level: Easy
Points: 100
"""
NUMBER_DIGIT = 50


def print_result(result):
    for element in result:
        print(element)


def find_sum(n):
    sum_array = NUMBER_DIGIT * [0]
    result_array = NUMBER_DIGIT * [0]
    number_array = [input().strip() for _ in range(n)]
    for number in number_array:
        for i, digit in enumerate(number):
            sum_array[NUMBER_DIGIT - 1 - i] += int(digit)

    rest = 0
    for i, sum_digits in enumerate(sum_array):
        sum_digits += rest
        result_array[i] = sum_digits % 10
        rest = (sum_digits // 10)

    while rest != 0:
        result_array.append(rest % 10)
        rest //= 10

    result = ""
    for i in range(len(result_array) - 1, len(result_array) - 11, -1):
        result += str(result_array[i])

    return result


n = int(input().strip())
result = find_sum(n)
print(result)
