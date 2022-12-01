def inp():
    arr = []
    for line in open("input_d11.txt", "rt"):
        line = line.replace("\n", "")
        tmp = []
        for char in line:
            tmp.append(int(char))
        arr.append(tmp)
    return arr

def increase(values):
    for i in range(len(values)):
        for j in range(len(values)):
            values[i][j] += 1

def reset_flashed(values):
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i][j] > 9:
                values[i][j] = 0
    return values
                
def increase_adjecent(i,j,values):

    if i != 0:
        values[i-1][j] += 1
        if j != 0:
            values[i-1][j-1] += 1
        if j != len(values[i])-1:
            values[i-1][j+1] += 1

    if i != len(values)-1:
        values[i+1][j] += 1
        if j != 0:
            values[i+1][j-1] += 1
        if j != len(values[i])-1:
            values[i+1][j+1] += 1
    if j != 0:
        values[i][j-1] += 1
    if j != len(values[i])-1:
        values[i][j+1] += 1

def info(values):
    for row in values:
        print(row)
    print("")

def count_flashed(flashed):
    count = 0
    for row in flashed:
        for val in row:
            if val:
                count += 1
    return count

def check_all(flashed):
    for row in flashed:
        for val in row:
            if val == False:
                return False
    return True

values = inp()
step = 1

info(values)

while True:

    flashed = [[False for j in range(len(values[i]))]for i in range(len(values))]

    increase(values)
    
    last_count = count_flashed(flashed)

    for i in range(len(values)):
        for j in range(len(values[i])):
            if values[i][j] > 9 and flashed[i][j] == False:
                increase_adjecent(i,j,values)
                flashed[i][j] = True

    count = count_flashed(flashed)

    while last_count != count:
        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j] > 9 and flashed[i][j] == False:
                    increase_adjecent(i,j,values)
                    flashed[i][j] = True
        last_count = count
        count = count_flashed(flashed)

    values = reset_flashed(values)

    if check_all(flashed):
        break
    
    step += 1

info(values)

print(step)








            
