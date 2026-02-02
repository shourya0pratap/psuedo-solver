# dictionary to store variables as key value pairs
variables = {}

def getValue(token:str):
    if token in variables:
        return variables[token]
    if token.startswith('"') and token.endswith('"'):
        return token.strip('"')
    if token == "True": return True
    if token == "False": return False
    try:
        if "." in token:
            return float(token)
        return int(token)
    except ValueError:
        print(f"ERROR: '{token}' is not a defined variable or valid number.")

def createVariable(instruction):
    type = instruction[1]
    var = instruction[2]
    val = " ".join(instruction[4:])
    match(type):
        case "INT":
            val = int(val)
        case "FLOAT":
            val = float(val)
        case "STR":
            val = val.strip('"')
            pass
        case "BOOL":
            val = bool(val)
    variables[var] = val

def setVariable(instruction):
    var = instruction[1]
    val = getValue(instruction[3])
    variables[var] = val

def addInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # add val TO var
    variables[var] += val
    
def subInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # subtract val FROM var
    variables[var] -= val
    
def mulInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    # multiply var WITH val
    variables[var] *= val

def remInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    # modulus var BY val
    variables[var] %= val

def divInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    # divide var BY val
    variables[var] /= val

def expInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    # raise var TO val
    variables[var] **= val

def inputInstruct(instruction:list[str]):
    var = instruction[1]
    dataType = instruction[3]
    val = input(f"Enter value for {var}: ")
    match dataType:
        case "INT":
            val = int(val) 
        case "FLOAT":
            val = float(val)
        case "BOOL":
            val = bool(val)
    variables[var] = val

def outputInstruct(instruction:list[str]):
    out = " ".join(instruction[1:])
    if out.startswith('"'):
        out = out.strip('"')
    elif out in variables:
        out = variables[out]
    print(out)

def evalCondition(instruction:list[str])->bool:
    arg1 = getValue(instruction[1])
    op = instruction[2]
    arg2 = getValue(instruction[3])
    flag = False
    match op:
        case "EQ":
            flag = arg1 == arg2
        case "NE":
            flag = arg1 != arg2
        case "LT":
            flag = arg1 < arg2  # type: ignore
        case "GT":
            flag = arg1 > arg2  # type: ignore
        case "LE":
            flag = arg1 <= arg2 # type: ignore
        case "GE":
            flag = arg1 >= arg2 # type: ignore
    return flag

def main(st:str):
    instructions =  st.split("\n")
    n = len(instructions)
    instPtr = 1  
    while(instPtr < n):
        instructStr = instructions[instPtr].split()
        if len(instructStr) == 0:
            continue
        match(instructStr[0]):
            case "LET":
                createVariable(instructStr)
            case "SET":
                setVariable(instructStr)
            case "ADD":
                addInstruct(instructStr)
            case "SUB":
                subInstruct(instructStr)
            case "MUL":
                mulInstruct(instructStr)
            case "REM":
                remInstruct(instructStr)
            case "DIV":
                divInstruct(instructStr)
            case "EXP":
                expInstruct(instructStr)
            case "INPUT":
                inputInstruct(instructStr)
            case "OUTPUT" | "PRINT":
                outputInstruct(instructStr)
            case "IF":
                flag = evalCondition(instructStr)
                if not flag:
                    ifCounter = 1
                    while (ifCounter > 0):
                        instPtr += 1
                        instructStr = instructions[instPtr].split()
                        if(instructStr[0]) == "IF":
                            ifCounter += 1
                        elif(instructStr[0] == "ENDIF"):
                            ifCounter -=1
        instPtr += 1

st = """
PRINT "HELLO WORLD"
"""
main(st)