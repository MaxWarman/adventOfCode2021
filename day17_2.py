def inp():
    for line in open("input_d17.txt", "rt"):
        line = line.replace("\n", "")
        line = line.split(": ")[1].split(", ")
        line[0] = line[0].replace("x=", "")
        line[1] = line[1].replace("y=", "")
        line[0] = line[0].split("..")
        line[1] = line[1].split("..")
        for i in range(len(line)):
            for j in range(len(line[i])):
                line[i][j] = int(line[i][j])
        return line

def check(i,j,velocity,area):
    global counter
    x = y = 0
    v = [i,j]
    v_init = v.copy()

    while x <= max(area[0]) and y >= min(area[1]):
        x += v[0]
        y += v[1]

        if v[0] > 0:
            v[0] -= 1
        elif v[0] < 0:
            v[0] += 1

        v[1] -= 1
            
        if (x >= area[0][0] and x <= area[0][1]) and (y >= area[1][0] and y <= area[1][1]):
            #print(f"Target reached for v: {v_init} at: x={x} y = {y}")
            velocity.append(v_init.copy())
            counter += 1
            return
        

    #print(f"Target not reached for v: {v}")
    return


if __name__ == "__main__":
    #area; [ [x_min, x_max], [y_min, y_max] ]
    area = inp()

    velocity = []
    counter = 0
    print(area)
    for i in range(-230, 330):
        for j in range(-150, 150):
            check(i,j,velocity,area)

    print(len(velocity))
