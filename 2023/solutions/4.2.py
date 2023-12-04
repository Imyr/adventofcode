with open("2023/inputs/4.txt") as file:
    cards = file.readlines()

mult = {}
for x in range(len(cards)):
    mult[x] = 1

total = 0
for i in range(len(cards)):
    info = cards[i].strip().split(": ")[1].split(" | ")
    winner = info[0].split(" ")
    have = info[1].split(" ")
    wins = 0
    for j in winner:
        if j in have and j.isdigit():
            wins += 1

    for y in range(wins):
        try:
            mult[i+1+y] += mult[i]
        except:
            pass

    total += mult[i]
    
print(total)

