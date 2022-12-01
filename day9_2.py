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

def find_basin(i, j, values, visited):    

    if values[i][j] == 9:
        return

    visited[i][j] = 1

    if visited[i-1][j] == 0 and values[i][j] < values[i-1][j]:
            size = find_basin(i-1, j, values, visited)
            
    if visited[i+1][j] == 0 and values[i][j] < values[i+1][j]:
            size = find_basin(i+1, j, values, visited) 

    if visited[i][j-1] == 0 and values[i][j] < values[i][j-1]:
            size = find_basin(i, j-1, values, visited)

    if visited[i][j+1] == 0 and values[i][j] < values[i][j+1]:
            size = find_basin(i, j+1, values, visited)

def find_three_biggest(sizes):
    m = []
    for i in range(3):
        ind = 0
        ma = sizes[0]
        for j in range(len(sizes)):
            if sizes[j] > ma:
                ma = sizes[j]
                ind = j
        m.append(sizes[ind])
        del sizes[ind]
    return m


values = inp()
sizes = []

for i in range(1, len(values)-1):
    
    for j in range(1, len(values[i])-1):
        
        if is_low_point(i, j, values):

            visited = [[0 for i in range(len(values[0]))] for j in range(len(values))]
            find_basin(i, j, values, visited)
            size = 0
            for row in visited:
                for val in row:
                    size += val
            sizes.append(size)

biggest = find_three_biggest(sizes)

res = 1
for val in biggest:
    res *= val
print(res)
