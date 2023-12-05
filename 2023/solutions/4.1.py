with open("2023/inputs/4.txt") as file:
    cards = file.readlines()

total = 0
for card in cards:
    info = card.strip().split(": ")[1].split(" | ")
    winner = info[0].split(" ")
    have = info[1].split(" ")
    wins = -1
    for i in winner:
        if i in have and i.isdigit():
            wins += 1
    total += 0 if wins==-1 else 2**wins

print(total)
