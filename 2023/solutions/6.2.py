import re

with open("2023/inputs/6.txt") as file:
    [time, distance] = file.readlines()

time = int(''.join(re.findall("(\S+)", time.split(":")[1].strip())))
distance = int(''.join(re.findall("(\S+)", distance.split(":")[1].strip())))

for pressed in range(1, time):
    d_t = pressed*(time-pressed)
    if d_t > distance:
        low = pressed
        break

for pressed in reversed(range(1, time)):
    d_t = pressed*(time-pressed)
    if d_t > distance:
        high = pressed
        break

print(high-low+1)
