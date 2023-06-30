"""
Task #5
Smallest multiple
Level: Medium
Points: 100
"""


def print_result(result):
    for element in result:
        print(element)



def computeGCD(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


def computeLCM(t):
    output_array = []

    for _ in range(t):
        n = int(input().strip())
        if n < 3:
            output_array.append(n)
        else:
            lcm = 2
            for i in range(3, n+1):
                gcd = computeGCD(lcm, i)
                lcm = (lcm * i) // gcd
            output_array.append(lcm)

    return output_array


t = int(input().strip())
result = computeLCM(t)
print_result(result)
