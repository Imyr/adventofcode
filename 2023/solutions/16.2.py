with open("2023/inputs/16.txt") as file:
    puzzle = [list(line) for line in file.read().strip().split("\n")]

from sys import setrecursionlimit
setrecursionlimit(3614)

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
    
energies = []
for i in range(110): 
    move(*[i, -1, i, 0])
    energies.append(sum([line.count("#") for line in energy]))
    energy = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
    dic = {}
    move(*[i, 110, i, 109])
    energies.append(sum([line.count("#") for line in energy]))
    energy = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
    dic = {}
    move(*[-1, i, 0, i])
    energies.append(sum([line.count("#") for line in energy]))
    energy = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
    dic = {}
    move(*[110, i, 109, i])
    energies.append(sum([line.count("#") for line in energy]))
    energy = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
    dic = {}

print(max(energies))
