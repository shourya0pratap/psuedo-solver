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
    val = instruction[4]
    match(type):
        case "INT":
            val = int(val)
        case "FLOAT":
            val = float(val)
        case "STR":
            val = str(val)
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
    val = getValue(instruction[1])
    var = instruction[3]
    # multiply var WITH val
    variables[var] *= val
    
def divInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # divide var BY val
    variables[var] /= val

def expInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
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
    out = "".join(instruction[1:])
    if out.startswith('"'):
        out = out.strip('"')
    elif out in variables:
        out = variables[out]
    print(out)

def main(st:str):
    instructions =  st.split("\n")  
    for instruction in instructions:
        instructStr = instruction.split()
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
            case "DIV":
                divInstruct(instructStr)
            case "EXP":
                expInstruct(instructStr)
            case "INPUT":
                inputInstruct(instructStr)
            case "OUTPUT":
                outputInstruct(instructStr)
st = "INPUT x as STR\nOUTPUT x"
main(st)