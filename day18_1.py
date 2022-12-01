def inp():
    tmp = []
    for line in open("input_d18.txt", "rt"):
        line = line.replace("\n", "")
        tmp.append(line)
    return tmp

def add(number1, number2):
    result = f"[{number1},{number2}]"
    return result

def reduce(number):
    pass

def explode(number):
    pass

def split(number):
    tmp = f"[{number//2},{number//2 + 1}]"
    return tmp

def put(p,i,ind):
    global values
    values[i] = values[i][:ind] + p + values[i][ind+1:]

values = inp()
print(add(values[0],values[1]))
print(split(7))
print(values[1])
put(split(3),1, 2)
print(values[1])
