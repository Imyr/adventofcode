with open("2023/inputs/2.txt") as file:
    games = [line.strip() for line in file.readlines()]

total = 0

for game in games:
    [id, turns] = game[5:].split(": ")
    max = [1, 1, 1]
    for turn in turns.split("; "):
        for cubes in turn.split(", "):
            [num, col] = cubes.split(" ")
            num = int(num)
            if (col=="red" and num>max[0]): max[0] = num
            elif (col=="green" and num>max[1]): max[1] = num
            elif (col=="blue" and num>max[2]): max[2] = num

    total += max[0]*max[1]*max[2]
    
print(total)
