import re

total = 0
with open("2023/inputs/1.txt") as file:
    for line in file.readlines():
        line = line.strip()
        match = re.match("^.*?([0-9]).*([0-9]).*?$", line)
        
        if match == None:
            match = re.match("^.*?([0-9]).*?$", line)
            one = match.group(1)
            two = match.group(1)
        else:
            one = match.group(1)
            two = match.group(2)

        total += int(one+two)
        
print(total)