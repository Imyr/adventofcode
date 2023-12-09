with open("2023/inputs/9.txt") as file:
    aps = [list(map(int, ap.split(" "))) for ap in file.read().strip().split("\n")]

total = 0
for ap in aps:
    list_of_all_differences = []
    old_difference = ap
    flag = 1  
    while flag:
        flag = 0
        list_of_all_differences.append(old_difference)
        difference = []
        for i in range(1, len(old_difference)):
            difference.append(old_difference[i]-old_difference[i-1])
        for j in difference:
            if j != 0:
                flag = 1
                break
        old_difference = difference

    subtract = 0
    for k in reversed(list_of_all_differences):
        subtract = k[0]-subtract
    total += subtract
    
print(total)
