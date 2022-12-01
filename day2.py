path = "input_d2.txt"

horizontal = aim = depth = 0
for line in open(path, "rt"):
    pair = line.split(" ")
    if pair[0] == "forward":
        horizontal += int(pair[1])
        depth += aim * int(pair[1])
    elif pair[0] == "up":
        aim -= int(pair[1])
    else:
        aim += int(pair[1])

print(horizontal,depth,horizontal*depth)
