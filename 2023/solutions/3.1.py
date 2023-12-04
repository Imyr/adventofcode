with open("2023/inputs/3.txt") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

total = 0

def print_digit(i, start, end):
    global total
    num = ""
    for j in range(start, end+1):
        num += matrix[i][j]

    j_start = 0 if start==0 else start-1
    j_end = len(matrix[i])-1 if end==len(matrix[i])-1 else end+1
    i_start = 0 if i==0 else i-1
    i_end = len(matrix)-1 if i==len(matrix)-1 else i+1

    flag = 0
    for i in range(i_start, i_end+1):
        for j in range(j_start, j_end+1):
            c = matrix[i][j]
            if not (c=='.' or c.isdigit()):
                flag = 1
                total += int(num)
                break
        if flag == 1:
            break


for i in range(len(matrix)):
    start = -1
    end = -1
    for j in range(len(matrix[i])):
        c = matrix[i][j]
        if c.isdigit():
            if start == -1:
                start = j
                end = j
            else:
                end = j
        else:
            if start != -1:
                print_digit(i, start, end)
                start = -1
                end = -1
            else:
                continue
    if start != -1:
        print_digit(i, start, end)
        start = -1
        end = -1

print(total)
