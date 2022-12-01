import binascii

def inp():
    txt = ""
    for line in open("input_d16.txt", "rt"):
        line = line.replace("\n", "")
        for i, char in enumerate(line):
            binChar = str(bin(int(char, base=16))).replace("0b", "")
            
            if len(binChar) < 4:
                binChar = "0" * (4-len(binChar)) + binChar
            txt += binChar
    return txt

def show(i):
    global values
    print("".join([char for char in values]))
    print("".join([" " if i != j else "^" for j in range(len(values))]))
    
def analyzeOperator(values, IDs, versions, literalValues):
    global i

    if "1" not in values[i:]:
        return
   
    I = None
    bits = None
    subPacketLen = None
    subPacketNum = None

    # Define length type ID
    if values[i] == "0":
        I = values[i]
        bits = 15
    elif values[i] == "1":
        I = values[i]
        bits = 11

    i+=1

    if I == "0":
        subPacketsLen = int(values[i:i+bits],2)
        
        counter = 0
        subtract = i
        i+=bits

        while counter < subPacketsLen:
            if isOperator(values, versions, IDs):
                #print(f"Operator at: {i}/{len(values)}")
                #show(i)
                analyzeOperator(values,IDs,versions,literalValues)
                counter = i - subtract
                #print(f"counter: {counter}/{subPacketsLen}")

            else:
                #print(f"Literal Value at: {i}/{len(values)}")
                #show(i)
                analyzeLiteralValue(values, literalValues)
                counter = i - subtract
                #print(f"counter: {counter}/{subPacketsLen}")
                
    elif I == "1":
        subPacketNum = int(values[i:i+bits],2)
        #print(f"subPacketNum: {subPacketNum}")
        i+=bits

        for j in range(subPacketNum):
            if i < len(values) - 1:
                if isOperator(values, versions, IDs):
                    #print(f"Operator at: {i}/{len(values)}")
                    #show(i)
                    analyzeOperator(values,IDs,versions,literalValues)
                else:
                    #print(f"Literal Value at: {i}/{len(values)}")
                    #show(i)
                    analyzeLiteralValue(values, literalValues)

def analyzeLiteralValue(values, literalValues):
    global i

    #if "1" not in values[i:]:
    #   return

    literalValue = ""
            
    bits = 5
            
    while values[i] == "1":
        literalValue += values[i+1:i+bits]
        i += bits
    else:
        literalValue += values[i+1:i+bits]
        i += bits

    literalValue = int(literalValue,2)
    
    literalValues.append(literalValue)


def isOperator(values, versions, IDs):
    global i
    #print(i, len(values))
    #show(i)
    versions.append(int(values[i:i+3], 2))
    IDs.append(int(values[i+3:i+6], 2))

    i += 6
    if IDs[-1] != 4:
        return True
    else:
        return False

values = inp()

literalValues = []
    
#versions
versions = []
lenVersion = 3

#IDs
IDs = []
lenID = 3

i = 0

if isOperator(values, versions, IDs):
    #print(f"Operator at: {i}/{len(values)}")
    #show(i)
    analyzeOperator(values, IDs, versions, literalValues)
else:
    #print(f"Literal value at: {i}/{len(values)}")
    #show(i)
    analyzeLiteralValue(values,literalValues)

print("\n\n\n")
print(f"Versions: {versions}")
print(f"IDs: {IDs}")
print(f"Literal values: {literalValues}")
print(sum(versions))
