"""
Task #15
Special Pythagorean triplet
Level: Easy
Points: 100
"""
MAX_SIZE = 500


def print_result(result):
    for element in result:
        print(element)


def get_dict_number_moves(max_size):
    dict_moves = [[0 for _ in range(max_size + 1)] for _ in range(max_size + 1)]
    for i in range(max_size + 1):
        dict_moves[1][i] = i + 1
        dict_moves[i][1] = dict_moves[1][i]

    for i in range(2, max_size + 1):
        for j in range(i, max_size):
            dict_moves[i][j] = (dict_moves[i][j - 1] + dict_moves[i - 1][j]) % (10 ** 9 + 7)
            dict_moves[j][i] = dict_moves[i][j]

    return dict_moves


def find_number_moves(t):
    output_array = []
    dict_moves = get_dict_number_moves(MAX_SIZE)
    for _ in range(t):
        n, m = input().strip().split(' ')
        output_array.append(dict_moves[int(n)][int(m)])

    return output_array


t = int(input().strip())
result = find_number_moves(t)
print_result(result)
