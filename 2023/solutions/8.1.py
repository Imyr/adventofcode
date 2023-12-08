with open("2023/inputs/8.txt") as file:
    [direction, maps] = file.read().split("\n\n")

direction = direction.strip()
maps = {map.split(" = ")[0]: map.split(" = ")[1][1:-1].split(", ") for map in maps.strip().split("\n")}

i = 0
total = 0
check = 'AAA'
while True:
    if direction[i]=='L':
        check = maps[check][0]
    else:
        check = maps[check][1]
    
    total += 1
    if check == 'ZZZ':
        break
    i+=1
    if i==len(direction):
        i=0

print(total)