with open("2023/inputs/8.txt") as file:
    [direction, maps] = file.read().split("\n\n")

direction = direction.strip()
maps = {map.split(" = ")[0]: map.split(" = ")[1][1:-1].split(", ") for map in maps.strip().split("\n")}

starts = []
for a_map in maps.keys():
    if a_map[-1] == 'A':
        starts.append(a_map)

ends = []
for check in starts:
    i = 0
    total = 0
    while True:
        if direction[i]=='L':
            check = maps[check][0]
        else:
            check = maps[check][1]
        
        total += 1
        if check[-1] == 'Z':
            break
        i+=1
        if i==len(direction):
            i=0

    ends.append(total)

flag = 1
for each in ends:
    if each%len(direction) != 0:
        flag = 0 
        break

if flag:
    from math import lcm
    print(lcm(*ends))
    
else:
    i = 0
    total = 0
    while True:
        for j in range(0, len(starts)): 
            if direction[i]=='L':
                starts[j] = maps[starts[j]][0]
            else:
                starts[j] = maps[starts[j]][1]
        total += 1

        flag = 1
        for k in range(0, len(starts)): 
            if starts[k][-1] != 'Z':
                flag = 0
        if flag==1:
            break
        
        i+=1
        if i==len(direction):
            i=0
        
    print(total)
    