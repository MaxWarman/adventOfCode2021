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
    global h
    x = y = 0
    v = [i,j]
    velocity.append([v.copy(), y])
    
    while x <= area[0][1] and y > area[1][1]:
        x += v[0]
        y += v[1]

        if v[0] > 0:
            v[0] -= 1
        elif v[0] < 0:
            v[0] += 1

        v[1] -= 1

        #print(x,y)
        
        if y > velocity[-1][1]:
            velocity[-1][1] = y
            
        if x >= area[0][0] and x <= area[0][1] and y >= area[1][0] and y <= area[1][1]:
            h.append(velocity[-1][1])
            return

    #print(f"Target not reached for v: {v}")
    velocity = velocity[:-1]
    return

#area [ [x_min, x_max], [y_min, y_max] ]
area = inp()

velocity = []
h = []

for i in range(1, 100):
    for j in range(1, 100):
        check(i,j,velocity,area)

print(max(h))
