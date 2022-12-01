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
        fuel += abs(act_pos - positions[i])
    return fuel

positions = inp()
print(positions)

flag = True
min_fuel = 0
opt_pos = positions[0]

for pos in positions:
    fuel = getFuelOnPosition(positions, pos)
    if flag:
        min_fuel = fuel
        flag = False
    else:
        if fuel < min_fuel:
            min_fuel = fuel
            opt_pos = pos

print(min_fuel, opt_pos, sep='\t')
