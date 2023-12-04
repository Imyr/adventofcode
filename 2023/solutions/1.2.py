import re

total = 0
with open("2023/inputs/1.txt") as file:
    for line in file.readlines():
        line = line.strip()
        match = re.match("^.*?(one|two|three|four|five|six|seven|eight|nine|[0-9]).*(one|two|three|four|five|six|seven|eight|nine|[0-9]).*?$", line)
        if match == None:
            match = re.match("^.*?(one|two|three|four|five|six|seven|eight|nine|[0-9]).*?$", line)
            one = match.group(1)
            two = match.group(1)
        else:
            one = match.group(1)
            two = match.group(2)

        one = one.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
        two = two.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
        total += int(one+two)
        
print(total)
