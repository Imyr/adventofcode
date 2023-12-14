with open("2023/inputs/14.txt") as file:
    platform = [list(line) for line in file.read().strip().split("\n")]

def rotate(platform):
    platform = list(map(lambda x: x[::-1], platform))

def tilt(platform):
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

for _ in range(200):
    tilt(platform)
    platform = [list(line[::-1])for line in zip(*platform)]
    tilt(platform)
    platform = [list(line[::-1])for line in zip(*platform)]
    tilt(platform)
    platform = [list(line[::-1])for line in zip(*platform)]
    tilt(platform)
    platform = [list(line[::-1])for line in zip(*platform)]

    total = 0
    mult = len(platform)
    for line in platform:
        total += mult*len([x for x in line if x == 'O'])
        mult -= 1

    print(total)

# https://files.catbox.moe/y92mnt.jpg
