"""""
Task #11
Largest product in a grid
Level: Easy
Points: 100
"""
import math


GRID_SIZE = 20
MINI_GRID_SIZE = 4


def diagonal_mini_grid(mini_grid):
    diagonal, diagonal_rev = [], []

    for i in range(MINI_GRID_SIZE):
        diagonal.append(mini_grid[i][i])
        diagonal_rev.append(mini_grid[i][MINI_GRID_SIZE - i - 1])

    return max(math.prod(diagonal), math.prod(diagonal_rev))


def find_max_product():
    grid = []

    for _ in range(GRID_SIZE):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)

    max_diagonal = max([diagonal_mini_grid([grid[i + k][j:j + MINI_GRID_SIZE] for k in range(MINI_GRID_SIZE)])
                        for i in range(GRID_SIZE - MINI_GRID_SIZE + 1)
                        for j in range(GRID_SIZE - MINI_GRID_SIZE + 1)])

    max_vertical = max([math.prod([grid[i + k][j] for k in range(MINI_GRID_SIZE)])
                        for i in range(GRID_SIZE - MINI_GRID_SIZE + 1)
                        for j in range(GRID_SIZE)])

    max_horizontal = max([math.prod([grid[i][j + k] for k in range(MINI_GRID_SIZE)])
                          for i in range(GRID_SIZE)
                          for j in range(GRID_SIZE - MINI_GRID_SIZE + 1)])

    return max(max_diagonal, max_horizontal, max_vertical)


result = find_max_product()
print(result)
