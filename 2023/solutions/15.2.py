with open("2023/inputs/15.txt") as file:
    strings = file.read().strip().split(",")

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h = (h*17)%256
    return h

dic_h = {}
dic_f = {}

total = 0
for string in strings:
    if '=' in string:
        (label, fl) = (string.split('=')[0], string.split('=')[1])
        dic_f[label] = int(fl)
        try: 
            if label not in dic_h[hash(label)]:
                dic_h[hash(label)].append(label)
        except KeyError:
            dic_h[hash(label)] = []
            dic_h[hash(label)].append(label)

    elif '-' in string:
        label = string.split('-')[0]
        try:    
            dic_f.pop(label)
            dic_h[hash(label)].remove(label)
            if dic_h[hash(label)] == []:
                dic_h.pop(hash(label))
        except KeyError:
            pass

total = 0
for _, (k, v) in enumerate(dic_h.items()):
    for idx in range(len(v)):
        total += (k+1)*(idx+1)*(dic_f[v[idx]])
print(total)