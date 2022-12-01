def inp():
    pairs = []
    for line in open("input_d5.txt", "rt"):
        tmp = line.split(" -> ")
        tmp[1] = tmp[1].replace("\n", "")

        for i in range(len(tmp)):
            tmp[i] = tmp[i].split(",")

        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] = int(tmp[i][j])
        pairs.append([tuple(tmp[0]),tuple(tmp[1])])
    return pairs


def find_max(pairs):
    max_x = max_y = 0
    for arr in pairs:
        for tupl in arr:
            if tupl[0] > max_x:
                max_x = tupl[0]
            if tupl[1] > max_y:
                max_y = tupl[1]
    return (max_x+1, max_y+1)   #both +1 because we need to include '0' coordinate

def info(arr):
    for row in arr:
        print(row)
    print("")

def display_board(board):
    for row in board:
        for val in row:
            if val == 0:
                print(".",end='')
            else:
                print(val,end='')
        print("")

def horiz(tuples, board):
    start = min(tuples[0][0], tuples[1][0])
    end = max(tuples[0][0], tuples[1][0])
    row_ind = tuples[0][1]
	
    for i in range(start, end+1):
        board[row_ind][i] += 1

def vert(tuples, board):
    start = min(tuples[0][1], tuples[1][1])
    end = max(tuples[0][1], tuples[1][1])
    col_ind = tuples[0][0]
    for i in range(start, end+1):
        board[i][col_ind] += 1

def diag_down(tuples, board):
    start_x = min(tuples[0][0], tuples[1][0])
    start_y = min(tuples[0][1], tuples[1][1])

    end_x = max(tuples[0][0], tuples[1][0])
    end_y = max(tuples[0][1], tuples[1][1])
	
    while start_x <= end_x and start_y <= end_y:
        board[start_y][start_x] += 1
        start_x += 1
        start_y += 1

def diag_up(tuples, board):
    start_x = min(tuples[0][0], tuples[1][0])
    start_y = max(tuples[0][1], tuples[1][1])

    end_x = max(tuples[0][0], tuples[1][0])
    end_y = min(tuples[0][1], tuples[1][1])

    while start_x <= end_x and start_y >= end_y:
        board[start_y][start_x] += 1
        start_x += 1
        start_y -= 1


def count_points(board):
    points = 0
    for row in board:
        for value in row:
            if value >= 2:
                points += 1
    return points
 
 

pairs = inp()
tmp = find_max(pairs)
max_x = tmp[0]
max_y = tmp[1]
del tmp

board = [[0 for i in range(max_x)] for j in range(max_y)]

for arr in pairs:
    x1, x2 = arr[0][0], arr[1][0]
    y1, y2 = arr[0][1], arr[1][1]
    if abs(x1 - x2) != 0 and abs(y1 - y2) == 0:
        horiz(arr, board)
        
    elif abs(y1 - y2) != 0 and abs(x1 - x2) == 0:
        vert(arr, board)
        
    elif abs(x1 - x2) == abs(y1 - y2) and ( (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2) ):
        diag_down(arr, board)

    elif abs(arr[0][0] - arr[1][0]) == abs(arr[0][1] - arr[1][1]) and ( (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2) ):
        diag_up(arr, board)


points = count_points(board)
print(points)














