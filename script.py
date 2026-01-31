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

def add(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # add val TO var
    variables[var] += val
    
def sub(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # subtract val FROM var
    variables[var] -= val
    
def mul(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # multiply var WITH val
    variables[var] *= val
    
def div(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # divide var BY val
    variables[var] /= val

def exp(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    # raise var TO val
    variables[var] **= val

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
                add(instructStr)
            case "SUB":
                sub(instructStr)
            case "MUL":
                mul(instructStr)
            case "DIV":
                div(instructStr)
            case "EXP":
                exp(instructStr)
        print(instruction, variables)  
st = "LET INT x BE 5\nLET FLOAT y BE 10\nSET x TO y"
main(st)