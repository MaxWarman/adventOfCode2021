def inp():
    tmp = []
    for line in open("input_d15.txt", "rt"):
        line = line.replace("\n", "")
        tmp.append([int(char) for char in line])
    return tmp

def info(arr):
    for row in arr:
        print(row)

def displayVisited(visited):
    for row in visited:
        for val in row:
            if val:
                print("x", end="")
            else:
                print(".", end="")
        print("")

def findPath(i, j, values, visited, path):
    global paths
    
    visited[i][j] = True
    path += values[i][j]

    if i == len(values) - 2 and j == len(values[0]) - 2:
        path += values[i][j]
        paths.append(path)
        #displayVisited(visited)
        visited[i][j] = False     
        return

    if visited[i-1][j] == True and visited[i+1][j] == True and visited[i][j-1] == True and visited[i][j+1] == True:
        visited[i][j] = False
        return

    if visited[i-1][j] == False:
        findPath(i-1, j, values, visited, path)

    if visited[i+1][j] == False: 
        findPath(i+1, j, values, visited, path)

    if visited[i][j-1] == False:    
        findPath(i, j-1, values, visited, path)

    if visited[i][j+1] == False:    
        findPath(i, j+1, values, visited, path)

    visited[i][j] = False
    return

values = inp()

for row in values:
    row.insert(0, None)
    row.append(None)
values.insert(0, [None for i in range(len(values[0]))] )
values.append([None for i in range(len(values[0]))] )

#for row in values:
#    print(row)

visited = [[False for i in range(len(values[0]))] for j in range(len(values))]
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if j == 0 or j == len(visited[0])-1 or i == 0 or i == len(visited)-1:
            visited[i][j] = True

for row in visited:
    print(row)

paths = []

findPath(1,1,values,visited, 0)

print(paths)
print(min(paths))
