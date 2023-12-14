with open("2023/inputs/13.txt") as file:
    patterns = [pattern.split("\n") for pattern in file.read().strip().split("\n\n")]

total = 0
for pattern in patterns:
    for idx in range(1, len(pattern)):
        if pattern[idx-1] == pattern[idx]:
            c = 1
            flag = 1
            while idx-1-c >= 0 and idx+c < len(pattern):
                if pattern[idx-1-c] != pattern[idx+c]: 
                    flag = 0
                    break
                c += 1
            if flag:
                total += 100*idx
                break
    for idx in range(1, len(pattern[0])):
        if list(map(lambda x: x[idx-1], pattern)) == list(map(lambda x: x[idx], pattern)):
            c = 1
            flag = 1
            while idx-1-c >= 0 and idx+c < len(pattern[0]):
                if list(map(lambda x: x[idx-1-c], pattern)) != list(map(lambda x: x[idx+c], pattern)):
                    flag = 0
                    break
                c += 1
            if flag:
                total += idx
                break
print(total)
