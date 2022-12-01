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
            insertions.append([[char for char in line[0]], line[1]])

def insert(template, toInsert):
    for i in range(len(toInsert)-1, -1, -1):
        template.insert(toInsert[i][0], toInsert[i][1])

def toTxt(template):
    txt = ""
    for val in template:
        txt += val
    print(txt)

def countScore(template):
    d = {}
    for char in template:
        if char not in d.keys():
            d[char] = 1
        else:
            d[char] += 1
    return (max(d.values()) - min(d.values()))

template = []
insertions = []
inp(template, insertions)

step = 0
limit = 10


while step < limit:
    toInsert = []
    for i in range(len(template)-1):
        for j in range(len(insertions)):
            if template[i] == insertions[j][0][0] and template[i+1] == insertions[j][0][1]:
                toInsert.append([i+1, insertions[j][1]])
                break

    insert(template, toInsert)
    step += 1

score = countScore(template)
print(score)
