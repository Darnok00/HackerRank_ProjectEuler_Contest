"""
Task #2
Even Fibonacci numbers
"""


def sum_even_fib_numbers(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())
        prev_num, act_num, act_sum = 1, 1, 0
        while act_num <= n:
            if act_num % 2 == 0:
                act_sum += act_num
            prev_num, act_num = act_num, act_num + prev_num

        output_array.append(act_sum)

    return output_array


def print_result(result):
    for element in result:
        print(element)


t = int(input().strip())
result = sum_even_fib_numbers(t)
print_result(result)
