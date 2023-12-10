with open("2023/inputs/10.txt") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

# https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python

from operator import add
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

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
now = (prev[0], prev[1]+1)

points = []
while True:
    via = matrix[now[0]][now[1]]
    how = directions[via]
    if tuple(map(add, now, how[0])) != prev:
        destination = tuple(map(add, now, how[0]))
    else:
        destination = tuple(map(add, now, how[1]))
    points.append((now[0], now[1]))
    prev = now
    now = destination
    if matrix[now[0]][now[1]] == 'S':
        break

total = 0
polygon = Polygon(points)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        point = Point(i, j)
        if polygon.contains(point):
            total += 1

print(total)
