with open("2023/inputs/7.txt") as file:
    hands = file.readlines()

ranks = {
    "5": 1,
    "14": 2,
    "23": 3,
    "113": 4,
    "122": 5,
    "1112": 6,
    "11111": 7,
}

def house(hand):
    dic = {}
    for c in hand:
        try:
            dic[c] += 1
        except KeyError:
            dic[c] = 1

    joker_count = 0
    try: 
        joker_count = dic.pop('J')
    except KeyError:
        pass
    check = list(map(str, dic.values()))
    check.sort()
    try:
        check[-1] = f"{int(check[-1]) + int(joker_count)}"
    except IndexError:
        return 1
    return(ranks[''.join(check)])

set_map = dict((hand, int(bid)) for (hand, bid) in [hand.strip().split(" ") for hand in hands])

set = {}
for [hand, bid] in [hand.strip().split(" ") for hand in hands]:
    house_rank = house(hand)
    try:
        set[house_rank].append(hand)
    except KeyError:
        set[house_rank] = []
        set[house_rank].append(hand)

keys = list(set.keys())
keys.sort()

order = {card: idx for (idx, card) in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])}
sorted_set = {}
for key in keys:
    sorted_hands = set[key]
    sorted_set[key] = sorted(sorted_hands, key=lambda hand: tuple(map(lambda card: order[card], hand)))

final = []
for i in list(sorted_set.values())[::-1]:
    for j in i[::-1]:
        final.append(set_map[j])

total = 0
for (idx, bid) in enumerate(final):
    total += (idx+1)*bid

print(total)
