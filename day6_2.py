def input():
    values = []
    for val in open("input_d6.txt", "rt").read():
        if val != "," and val != "\n":
            values.append(int(val))

    tmp = [0 for i in range(9)]
    for val in values:
        tmp[val] += 1
    return tmp
    

def rotate(arr):
    tmp = arr[0]
    del arr[0]
    arr.append(tmp)
    arr[6] += tmp
    return arr
    

values = input()
day = 0
while day < 257:        
    values = rotate(values)
    day += 1
    if day == 80 or day == 256:
        print(sum(values))
