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
                return char
    return None


lines = inp()

points = { "]":57, "}":1197, ">":25137, ")":3, None:0}
result = 0
for line in lines:
    char = check_syntax(line)
    result += points[char]

print(result)
