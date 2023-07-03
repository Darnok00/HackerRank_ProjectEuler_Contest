"""
Task #14
Longest Collatz sequence
Level: Easy
Points: 100
"""
def print_result(result):
    for element in result:
        print(element)

def create_longest_sequence_dict(n):
    dict_collatz = {}
    dict_seq = {}
    max_value, max_index = 0, 0
    for i in range(1, n+1):
        counter = 1
        number = i
        while number != 1:
            if number in dict_seq:
                counter += (dict_seq[number] - 1)
                break

            counter += 1
            if number % 2 == 1:
                number = 3 * number + 1
            else:
                number //= 2

        value = counter
        dict_seq[i] = counter
        if value >= max_value:
            max_value = value
            max_index = i
            dict_collatz[i] = i
        else:
            dict_collatz[i] = max_index

    return dict_collatz


def find_difference(t):
    output_array, inputs = [], []
    for _ in range(t):
        inputs.append(int(input().strip()))

    dict_collatz = create_longest_sequence_dict(max(inputs))
    for n in inputs:
        output_array.append(dict_collatz[n])

    return output_array


t = int(input().strip())
result = find_difference(t)
print_result(result)
