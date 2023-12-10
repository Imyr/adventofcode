with open("2023/inputs/10.txt") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

from operator import add
from copy import deepcopy

matrix_template = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

directions = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
}

prev = (0, 0)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'S':
            prev = (i, j)

# Manually checking which two pipes connect to S
nows = [(prev[0], prev[1]-1), (prev[0]+1, prev[1])]

matrices = []
for hi in nows:
    new_matrix = deepcopy(matrix_template)
    now = hi
    c = 1
    while True:
        via = matrix[now[0]][now[1]]
        how = directions[via]
        if tuple(map(add, now, how[0])) != prev:
            destination = tuple(map(add, now, how[0]))
        else:
            destination = tuple(map(add, now, how[1]))
        try:
            new_matrix[now[0]][now[1]] = c
        except IndexError:
            new_matrix[now[0]] = []
            new_matrix[now[0]][now[1]] = c
        prev = now
        now = destination
        c += 1
        if matrix[now[0]][now[1]] == 'S':
            new_matrix[now[0]][now[1]] = 0
            break
    matrices.append(new_matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix_template[i][j] = min(matrices[0][i][j], matrices[1][i][j])

maxi = -1
for i in matrix_template:
    for j in i:
        if j > maxi:
            maxi = j

print(maxi)
