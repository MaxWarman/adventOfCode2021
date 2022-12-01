def inp():
    pairs = []
    folds = []
    f = False
    for line in open("input_d13.txt", "rt"):
        if line == "\n":
            f = True
            continue

        line = line.replace("\n", "")
        
        if f == False:
            line = line.split(",")
            pairs.append((int(line[0]),int(line[1])))
        else:
            line = line.split(" ")
            folds.append(line[2])

    max_x = 0
    max_y = 0

    for i in range(len(pairs)):
        if pairs[i][0] > max_x:
            max_x = pairs[i][0]
        if pairs[i][1] > max_y:
            max_y = pairs[i][1]

    max_x += 1
    max_y += 1
    
    arr = [[0 for i in range(max_x)] for j in range(max_y)]

    for pair in pairs:
        arr[pair[1]][pair[0]] += 1

    return (arr, folds)

def info(a):
    for row in a:
        print(row)
    print("")

def countDots(arr):
    dots = 0
    for row in arr:
        for val in row:
            if val > 0:
                dots += 1
    return dots

def printDots(arr):
    for row in arr:
        for val in row:
            if val > 0:
                print("#",end="")
            else:
                print(" ",end="")
        print("")
def fold_x(arr, x):
    tmp = [[0 for i in range(x)] for j in range(len(arr))]
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] = arr[i][j]

    tmp2 = arr.copy()
    for i in range(len(tmp2)):
        for j in range(x+1):
            del tmp2[i][0]

    y = len(tmp2[0])-1
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] += tmp2[i][y-j]
    return tmp
    
def fold_y(arr, y):
    tmp = [[0 for i in range(len(arr[0]))] for j in range(y)]
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] = arr[i][j]

    tmp2 = arr.copy()
    for i in range(y+1):
        del tmp2[0]

    x = len(tmp2)-1
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] += tmp2[x-i][j]
        
    return tmp

        
arr = inp()[0]
folds = inp()[1]

for fold in folds:
    f = fold.split("=")
    #info(arr)
    if f[0] == "x":
        arr = fold_x(arr, int(f[1]))
    elif f[0] == "y":
        arr = fold_y(arr, int(f[1]))

printDots(arr)
dots = countDots(arr)
print(dots)






