with open("2023/inputs/11.txt") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

for j in range(len(matrix[0])-1, -1, -1):
    for i in range(len(matrix)):
        if matrix[i][j] == "#":
            break
    else:
        for i in range(len(matrix)):
            matrix[i].insert(j, ".")

for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            break
    else:
        matrix.insert(i, ["." for _ in range(len(matrix[0]))])

points = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            points.append((i, j))

total = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        total += (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))

print(total)
