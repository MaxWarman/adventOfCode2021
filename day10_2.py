def inp():
    tmp = []
    for line in open("input_d10.txt", "rt"):
        line = line.replace("\n", "")
        tmp.append(line)
    return tmp

def check_syntax(line):
    last_opened = [line[0]]
    for char in line[1:]:
        if char in "[{<(":
            last_opened.append(char)
        elif char in "]}>)":
            if (last_opened[-1] == "[" and char == "]") or (last_opened[-1] == "{" and char == "}") or (last_opened[-1] == "(" and char == ")") or (last_opened[-1] == "<" and char == ">"):
                del last_opened[-1]
                continue
            else:
                return False
    return True

def find_missing(line):
    last_opened = [line[0]]
    for char in line[1:]:
        if char in "[{<(":
            last_opened.append(char)
        elif char in "]}>)":
            if (last_opened[-1] == "[" and char == "]") or (last_opened[-1] == "{" and char == "}") or (last_opened[-1] == "(" and char == ")") or (last_opened[-1] == "<" and char == ">"):
                del last_opened[-1]
                continue

    txt = ""
    for i in range(len(last_opened)-1, -1, -1):
        if last_opened[i] == "[":
            txt += "]"
        elif last_opened[i] == "{":
            txt += "}"
        elif last_opened[i] == "<":
            txt += ">"
        elif last_opened[i] == "(":
            txt += ")"
             
    return txt

def sort(arr):
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

lines = inp()

inds = []
for i in range(len(lines)):
    if check_syntax(lines[i]) == False:
        inds.insert(0, i)

for ind in inds:
    del lines[ind]

scores = []
points = { ")":1, "]":2, "}":3, ">":4}
for line in lines:
    missing = find_missing(line)
    tmp = 0
    for char in missing:
        tmp = 5*tmp + points[char]
    scores.append(tmp)

scores = sort(scores)

print(scores[len(scores)//2])
