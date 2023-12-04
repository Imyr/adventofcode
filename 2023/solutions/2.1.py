with open("2023/inputs/2.txt") as file:
    games = [line.strip() for line in file.readlines()]

total = 0
r = 12
g = 13
b = 14

for game in games:
    [id, turns] = game[5:].split(": ")
    flag = 1
    for turn in turns.split("; "):
        for cubes in turn.split(", "):
            [num, col] = cubes.split(" ")
            num = int(num)
            if (col=="red" and num>r) or (col=="green" and num>g) or (col=="blue" and num>b):
                flag=0
                break
    
    if flag==1:
        total += int(id)

print(total)
