def inp():
    arr = []
    for line in open("input_d9.txt", "rt"):
        line = line.replace("\n", "")
        tmp = []
        for char in line:
            tmp.append(int(char))
        arr.append(tmp)
        del tmp
        
    for i in range(len(arr)):
        arr[i].insert(0,9)
        arr[i].append(9)
    tmp = [9 for i in range(len(arr[0]))]
    arr.insert(0, tmp)
    arr.append(tmp)
    return arr

def is_low_point(i, j, values):
    return values[i][j] < values[i-1][j] and values[i][j] < values[i+1][j] and values[i][j] < values[i][j-1] and values[i][j] < values[i][j+1]

values = inp()
low_points = []

for i in range(1, len(values)-1):
    for j in range(1, len(values[i])-1):
        if is_low_point(i, j, values):
            low_points.append(values[i][j])

res = 0
for value in low_points:
    res += value + 1

print(res)
