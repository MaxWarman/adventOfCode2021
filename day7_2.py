def inp():
    pos = []
    for line in open("input_d7.txt", "rt"):
        line = line.replace("\n", "")
        line = line.split(",")
        for val in line:
            pos.append(int(val))
    return pos

def getFuelOnPosition(positions, act_pos):
    fuel = 0
    for i in range(len(positions)):
        distance = abs(act_pos - positions[i])
        fuel += distance * (distance + 1) // 2
    return fuel

positions = inp()
print(positions)

flag = True
min_fuel = 0
opt_pos = positions[0]

for i in range(max(positions)):
    fuel = getFuelOnPosition(positions, i)
    if flag:
        min_fuel = fuel
        flag = False
    else:
        if fuel < min_fuel:
            min_fuel = fuel
            opt_pos = i

print(min_fuel, opt_pos, sep='\t')
