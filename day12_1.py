def inp():
    d = {}
    for line in open("input_d12.txt", "rt"):
        line = line.replace("\n", "")
        line = line.split("-")

        if line[0] not in d.keys():
            d[line[0]] = [line[1]]
        else:
            d[line[0]].append(line[1])

        if line[1] not in d.keys():
            d[line[1]] = [line[0]]
        else:
            d[line[1]].append(line[0])
       
    return d

def info(d):
    for key in d.keys():
        print(f"{key} -> {d[key]}")

def makeVisited(graph):
    tmp = {}
    for key in graph.keys():
         tmp[key] = False
    return tmp

def visitNode(name, graph, visited):
    global f
    
    global path
    path.append(name)

    #for val in path:
    #    print(f"{val} ", end="")
    #print("")
    
    if visited[name]:

        del path[-1]
        #print(f"*going back*\tvisited[{name}]==True\n")
        #for val in path:
        #    print(f"{val} ", end="")
        #print("")

        return

    if name != name.upper():
        visited[name] = True

    if name == "end":
        visited[name] = False
        
        global paths
        paths += 1

        global endpaths
        endpaths.append(path.copy())
        
        del path[-1]
        #print(f"*going back*\tname=='end'\n")
        
        #for val in path:
        #    print(f"{val} ", end="")
        #print("")
        
        return

    if False not in [visited[n] for n in graph[name]]:
        visited[name] = False
        
        del path[-1]
        #print(f"*going back*\t{name} has no more neighbours\n")
        #for val in path:
        #    print(f"{val} ", end="")
        #print("")

        return

    for neighbour in graph[name]:
        isUppercase = (neighbour == neighbour.upper())
        if visited[neighbour] == False or isUppercase:
            visitNode(neighbour, graph, visited)

    visited[name] = False

    del path[-1]
    #print(f"*going back*\tend of funtion at {name}")

    return

graph = inp()
visited = makeVisited(graph)

endpaths = []

paths = 0
path = []

visitNode("start", graph, visited)

print(paths)

#for p in endpaths:
#    print(p)











