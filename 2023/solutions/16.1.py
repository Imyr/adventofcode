with open("2023/inputs/16.txt") as file:
    puzzle = [list(line) for line in file.read().strip().split("\n")]

from sys import setrecursionlimit
setrecursionlimit(3116)

energy = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
dic = {}

def move(pi, pj, ni, nj):
    
    if (pi, pj, ni, nj) in dic:
        return
    else:
        dic[(pi, pj, ni, nj)] = 1

    if 0 <= nj and nj < len(puzzle) and 0 <= ni and ni < len(puzzle[0]):
        energy[ni][nj] = '#'
    else:
        return

    if puzzle[ni][nj] == '.':
        if pj < nj and pi == ni:
            move(ni, nj, ni, nj+1)
        elif pj > nj and pi == ni:
            move(ni, nj, ni, nj-1)
        elif pj == nj and pi < ni:
            move(ni, nj, ni+1, nj)
        elif pj == nj and pi > ni:
            move(ni, nj, ni-1, nj)
        
    elif puzzle[ni][nj] == '/':
        if pj < nj and pi == ni:
            move(ni, nj, ni-1, nj)
        elif pj > nj and pi == ni:
            move(ni, nj, ni+1, nj)
        elif pj == nj and pi < ni:
            move(ni, nj, ni, nj-1)
        elif pj == nj and pi > ni:
            move(ni, nj, ni, nj+1)
    
    elif puzzle[ni][nj] == '\\':
        if pj < nj and pi == ni:
            move(ni, nj, ni+1, nj)
        elif pj > nj and pi == ni:
            move(ni, nj, ni-1, nj)
        elif pj == nj and pi < ni:
            move(ni, nj, ni, nj+1)
        elif pj == nj and pi > ni:
            move(ni, nj, ni, nj-1)
    
    elif puzzle[ni][nj] == '|':
        if pj < nj and pi == ni:
            move(ni, nj, ni-1, nj)
            move(ni, nj, ni+1, nj)
        elif pj > nj and pi == ni:
            move(ni, nj, ni-1, nj)
            move(ni, nj, ni+1, nj)
        elif pj == nj and pi < ni:
            move(ni, nj, ni+1, nj)
        elif pj == nj and pi > ni:
            move(ni, nj, ni-1, nj)
    
    elif puzzle[ni][nj] == '-':
        if pj < nj and pi == ni:
            move(ni, nj, ni, nj+1)
        elif pj > nj and pi == ni:
            move(ni, nj, ni, nj-1)
        elif pj == nj and pi < ni:
            move(ni, nj, ni, nj-1)
            move(ni, nj, ni, nj+1)
        elif pj == nj and pi > ni:
            move(ni, nj, ni, nj-1)
            move(ni, nj, ni, nj+1)

move(0, -1, 0, 0)
print(sum([line.count("#") for line in energy]))
