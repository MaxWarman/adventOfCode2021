path = "input.txt"

values = [int(line) for line in open(path, "rt")]
count_inc = 0
for i in range(3, len(values)):
    if values[i] > values[i-3]:
        count_inc += 1
print(count_inc)
