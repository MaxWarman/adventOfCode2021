def show_number(ind):
    if ind == [1,1,0,1,1,1,1]:
        return "0"
    elif ind == [0,0,0,1,0,0,1]:
        return "1"
    elif ind == [1,0,1,1,1,1,0]:
        return "2"
    elif ind == [1,0,1,1,0,1,1]:
        return "3"
    elif ind == [0,1,1,1,0,0,1]:
        return "4"
    elif ind == [1,1,1,0,0,1,1]:
        return "5"
    elif ind == [1,1,1,0,1,1,1]:
        return "6"
    elif ind == [1,0,0,1,0,0,1]:
        return "7"
    elif ind == [1,1,1,1,1,1,1]:
        return "8"
    elif ind == [1,1,1,1,0,1,1]:
        return "9"
    
    
numbers = []
patterns = []
sum = 0
for line in open("input_d8.txt", "rt"):
    line = line.split("|")

    patt = line[0]
    num = line[1]
      
    patt = patt.split(" ")
    del patt[-1]
    patterns.append(patt)
    
    num = num.split(" ")
    del num[0]
    num[-1] = num[-1].replace("\n", "")
    numbers.append(num)



for i in range(len(patterns)):
    possible_chars = ["" for x in range(10)]
    ind = ["" for x in range(7)]
    for val in patterns[i]:
        if len(val) == 2:
            possible_chars[1] = "".join(sorted(val))
        elif len(val) == 3:
            possible_chars[7] = "".join(sorted(val))

    # find ind[0]
    for char in possible_chars[7]:
        if char not in possible_chars[1]:
            if char not in ind[0]:
                ind[0] += char

    del possible_chars

    for char in "abcdefg":
        counter = 10
        for val in patterns[i]:
            if char not in val:
                counter -= 1
        if counter == 9:
            if char not in ind[6]:
                ind[6] += char
        elif counter == 8 and char != ind[0]:
            if char not in ind[3]:
                ind[3] += char
        elif counter == 7:
            if char not in ind[2]:
                ind[2] += char
            if char not in ind[5]:
                ind[5] += char
        elif counter == 6:
            if char not in ind[1]:
                ind[1] += char
        elif counter == 4:
            if char not in ind[4]:
                ind[4] += char

    zero = ""
    for code in patterns[i]:
        if len(code) == 6:
            if ind[3] in code and ind[4] in code:
                zero = code
                break
    tmp = ""
    for char in ind:
        if char != ind[2]:
            tmp += char
            
    for char in zero:
        if char not in tmp:
            ind[5] = char
            break

    for char in ind[2]:
        if char not in ind[5]:
            ind[2] = char
            break
    res = ""
    for num in numbers[i]:
        arr = [0 for x in range(7)]
        for j in range(len(ind)):
            if ind[j] in num:
                arr[j] += 1
        res += show_number(arr)

    res = int(res)
    print(res)
    sum += res
    
print(sum)












    
