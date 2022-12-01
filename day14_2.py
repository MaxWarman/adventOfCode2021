def inp(template, insertions):
    flag = True
    for line in open("input_d14.txt", "rt"):
        line = line.replace("\n", "")

        if line == "":
            flag = False
            continue

        if flag:
            for char in line:
                template.append(char)
        else:
            line = line.split(" -> ")
            insertions.append([line[0], line[1]])

def countScore(d):
    return (max(d.values()) - min(d.values()))

template = []
insertions = []
inp(template, insertions)


#create and fill d
d = {}
for char in template:
    if char not in d.keys():
        d[char] = 1
    else:
        d[char] += 1

#create and fill pairs
pairs = {}
for i in range(len(template)-1):
    pair = template[i]+template[i+1]
    if pair not in pairs.keys():
        pairs[pair] = 1
    else:
        pairs[pair] += 1


step = 0
limit = 40

while step < limit:
    toAppend = []
    for pair in pairs.keys():
            for i in range(len(insertions)):
                if pair == insertions[i][0] and pairs[pair] > 0:
                    toAppend.append([pair[0] + insertions[i][1], pairs[pair]])
                    toAppend.append([insertions[i][1] + pair[1], pairs[pair]])
                            
                    if insertions[i][1] not in d.keys():
                        d[insertions[i][1]] = pairs[pair]
                    else:
                        d[insertions[i][1]] += pairs[pair]

                    pairs[pair] = 0
                
    for pair in toAppend:
        if pair[0] not in pairs.keys():
            pairs[pair[0]] = pair[1]
        else:
            pairs[pair[0]] += pair[1]

    step += 1
    
    if step in (10, 40):
        for char in d.keys():
            print(f"{char}: {d[char]}")
        score = countScore(d)
        print(f"\nScore = {score}\n")

