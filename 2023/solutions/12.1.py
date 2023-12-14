with open("2023/inputs/12.txt") as file:
    arrangements = [(list(arrangement.split(" ")[0]), arrangement.split(" ")[1].split(",")) for arrangement in file.read().strip().split("\n")]

from copy import deepcopy
import re

total = 0
for arrangement in arrangements:
    replaceables = [i for i in range(len(arrangement[0])) if arrangement[0][i] == '?']
    
    reg = "^\.*"
    for i in arrangement[1]:
        reg += "#{" + i + "}\.+"
    reg = reg[:-1] + "*"
    reg += "$"

    for combination in range(2**len(replaceables)):
        new_arrangement = deepcopy(arrangement[0])
        c = combination
        for i in range(len(new_arrangement)):
            if new_arrangement[i] == "?":
                if c%2 == 0:
                    new_arrangement[i] = "."
                else:
                    new_arrangement[i] = "#"
                c//=2
        if re.match(reg, "".join(new_arrangement))!=None:
            total += 1

print(total)
