with open("2023/inputs/15.txt") as file:
    strings = file.read().strip().split(",")

total = 0
for string in strings:
    hash = 0
    for c in string:
        hash += ord(c)
        hash = (hash*17)%256
    total += hash

print(total)
