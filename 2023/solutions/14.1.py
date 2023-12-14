with open("2023/inputs/14.txt") as file:
    platform = [list(line) for line in file.read().strip().split("\n")]

for i in range(len(platform[0])):
    a = 0
    while a < len(platform):
        if platform[a][i] == '.':
            b = a + 1
            while b < len(platform):
                if platform[b][i] == 'O':
                    platform[a][i] = 'O'
                    platform[b][i] = '.'
                    break
                elif platform[b][i] == '#':
                    a = b
                    break
                b += 1
        a += 1

total = 0
mult = len(platform)
for line in platform:
    total += mult*len([x for x in line if x == 'O'])
    mult -= 1

print(total)
