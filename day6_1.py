def input():
    values = []
    for val in open("input_d6.txt", "rt").read():
        if val != "," and val != "\n":
            values.append(int(val))
    return values

values = input()

day = 0

dt = open("out.txt", "wt")

while day < 80:
    print(f"day {day}")
    l = len(values)
    for i in range(l):
        values[i] -= 1
        if values[i] < 0:
            values[i] = 6
            values.append(8)            
    dt.write(f"{str(len(values))}\n")
    day += 1
dt.close()    
    
print(len(values))
