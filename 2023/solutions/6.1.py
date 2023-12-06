import re

with open("2023/inputs/6.txt") as file:
    [time, distance] = file.readlines()

time = list(map(int, re.findall("(\S+)", time.split(":")[1].strip())))
distance = list(map(int, re.findall("(\S+)", distance.split(":")[1].strip())))

ways = []
for idx in range(0, len(time)):
    count = 0
    for pressed in range(1, time[idx]):
        d_t = pressed*(time[idx]-pressed)
        if d_t > distance[idx]:
            count += 1
    ways.append(count)

total = 1
for way in ways:
    total *= way

print(total)