def check_horizontal(board, count):
    for row in range(len(board)):
        bingo = True
        for col in range(len(board[row])):
            if count[row][col] == 0:
                    bingo = False
                    break
        if bingo == True:
            sum = 0
            for m in range(len(board)):
                for n in range(len(board[m])):
                    if count[m][n] == 0:
                        sum += int(board[m][n])
                    else:
                        continue
            return sum
    return 0

def check_vertical(board, count):
    for row in range(len(board)):
        bingo = True
        for col in range(len(board[row])):
            if count[col][row] == 0:
                    bingo = False
                    break
        if bingo == True:
            sum = 0
            for m in range(len(board)):
                for n in range(len(board[m])):
                    if count[m][n] == 0:
                        sum += int(board[m][n])
                    else:
                        continue
            return sum
    return 0

values = []
boards = []
flag = True
tmp = []
for line in open("input_d4.txt", "rt"):
    if flag:
        values = line.split(",")
        flag = False
    else:
        if line == "\n":
            continue
        else:
            x = []
            for value in line.split():
                x.append(value)
            tmp.append(x)
            if len(tmp) == 5:
                boards.append(tmp)
                tmp = []

for i in range(len(boards)):
    for j in range(len(boards[i])):
        for k in range(len(boards[i][j])):
           boards[i][j][k] = boards[i][j][k].replace("\n", "")

for i in range(len(values)):
    values[i] = values[i].replace("\n", "")

counts = [[[0 for k in range(len(boards[i][j]))]for j in range(len(boards[i]))]for i in range(len(boards))]

print(boards)
print(values)
print(counts)

for value in values:
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == value:
                    counts[i][j][k] += 1
    
    isRes = False
    for i in range(len(boards)):
        res = check_horizontal(boards[i],counts[i])
        if res != 0:
            isRes = True
            print(int(value))
            print(res)
            print(int(value) * res)
            break
        res = check_vertical(boards[i],counts[i])
        if res != 0:
            isRes = True
            print(int(value))
            print(res)
            print(int(value) * res)
            break
    if isRes:
        break


                       

        
