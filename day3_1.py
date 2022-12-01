gamma = epsilon = ""
l = 12
gamma_counts = [0 for i in range(l)]  
for line in open("input_d3.txt", "rt"):
    for i in range(len(line)-1):
        if line[i] == "0":
            gamma_counts[i] += 1
        else:
            gamma_counts[i] -= 1

for i in range(len(gamma_counts)):
    if gamma_counts[i] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
