def find_most_common(values, pos):
    counter = 0
    for value in values:
        if value[pos] == "1":
            counter += 1
        else:
            counter -= 1
    return counter

def find_oxygen(vals):
    i = 0
    values = list(vals)
    while len(values) > 1:
        common = None
        if find_most_common(values, i) >= 0:
            common = "1"
        else:
            common = "0"

        indices = []
        for j in range(len(values)):
            if values[j][i] != common:
                indices.append(j)

        for j in range(len(indices)-1, -1, -1):
            del values[indices[j]]
        i += 1
    return int(values[0], 2)

def find_co2(vals):
    i = 0
    values = list(vals)
    while len(values) > 1:
        l_common = None
        if find_most_common(values, i) < 0:
            l_common = "1"
        else:
            l_common = "0"

        indices = []
        for j in range(len(values)):
            if values[j][i] != l_common:
                indices.append(j)

        for j in range(len(indices)-1, -1, -1):
            del values[indices[j]]
        i += 1
    return int(values[0], 2)

values = [line for line in open("input_d3.txt", "rt")]
for i in range(len(values)):
    values[i] = values[i].replace("\n", "")

oxygen = find_oxygen(values)
co2 = find_co2(values)
print(oxygen*co2)
                
