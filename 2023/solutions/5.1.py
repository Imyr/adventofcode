with open("2023/inputs/5.txt") as file:
    maps = file.read().split("\n\n")

def return_value(dict, key):
    for kv in dict.split("\n"):
        kv = kv.strip().split(" ")
        kv = list(map(int, kv))
        if key in range(kv[1], kv[1]+kv[2]):
            return kv[0]+key-kv[1]
    return key

loc = []
seeds = maps[0].strip().split(": ")[1]        
for seed in list(map(int, seeds.split(" "))):
    temp = seed
    for i in range(1, 7+1):
        temp = return_value(maps[i].strip().split(":\n")[1], temp)
    loc.append(temp)
print(min(loc))  
