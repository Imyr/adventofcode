with open("2023/inputs/11.txt") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

empty_columns = []
for j in range(len(matrix[0])-1, -1, -1):
    for i in range(len(matrix)):
        if matrix[i][j] == "#":
            break
    else:
        empty_columns.append(j) 

empty_rows = []
for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            break
    else:
        empty_rows.append(i)

points = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            points.append((i, j))

total = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        add_to_i = 0
        for r in empty_rows:
            if r in range(min(points[i][0], points[j][0]), max(points[i][0], points[j][0])):
                add_to_i += 1
        add_to_j = 0
        for r in empty_columns:
            if r in range(min(points[i][1], points[j][1]), max(points[i][1], points[j][1])):
                add_to_j += 1
        total += ((add_to_i*999999)) + abs(points[i][0] - points[j][0]) + ((add_to_j*999999)) + abs(points[i][1] - points[j][1])

print(total)
