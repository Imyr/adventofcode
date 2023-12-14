with open("2023/inputs/13.txt") as file:
    patterns = [[list(line) for line in pattern.split("\n")] for pattern in file.read().strip().split("\n\n")]
def row(pattern, ch):
    for idx in range(1, len(pattern)):
        if pattern[idx-1] == pattern[idx] and ch!=idx:
            c = 1
            flag = 1
            while idx-1-c >= 0 and idx+c < len(pattern):
                if pattern[idx-1-c] != pattern[idx+c]: 
                    flag = 0
                    break
                c += 1
            if flag:
                return idx
    return -1

def column(pattern, ch):
    for idx in range(1, len(pattern[0])):
        if list(map(lambda x: x[idx-1], pattern)) == list(map(lambda x: x[idx], pattern)) and ch!=idx:
            c = 1
            flag = 1
            while idx-1-c >= 0 and idx+c < len(pattern[0]):
                if list(map(lambda x: x[idx-1-c], pattern)) != list(map(lambda x: x[idx+c], pattern)):
                    flag = 0
                    break
                c += 1
            if flag:
                return idx
    return -1

dic = {'#': ".", '.': '#'}

from copy import deepcopy

total = 0
for pattern in patterns:
    og = (row(pattern, -1), column(pattern, -1))
    flag = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            new_pattern = deepcopy(pattern)
            new_pattern[i][j] = dic[new_pattern[i][j]]
            new = (row(new_pattern, og[0]), column(new_pattern, og[1]))
            if new[0] != -1:
                total += 100*new[0]
                flag = 1
                break
            if new[1] != -1:
                total += new[1]
                flag = 1
                break
        if flag:
            break

print(total)
