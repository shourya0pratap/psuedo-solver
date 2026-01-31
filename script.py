# dictionary to store variables as key value pairs
variables = {}

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

def add(instruction):
    var1 = instruction[1]
    var2 = instruction[3]
    # add var1 TO var2
    variables[var2] += variables[var1]
    
def sub(instruction):
    var1 = instruction[1]
    var2 = instruction[3]
    # subtract var1 FROM var2
    variables[var2] -= variables[var1]
    
def mul(instruction):
    var1 = instruction[1]
    var2 = instruction[3]
    # multiply var1 WITH var2
    variables[var1] *= variables[var2]
    
def div(instruction):
    var1 = instruction[1]
    var2 = instruction[3]
    # divide var1 BY var2
    variables[var1]/=variables[var2]

def exp(instruction):
    var1 = instruction[1]
    var2 = instruction[3]
    # raise var1 TO var2
    variables[var1] **= variables[var2]

def main(st:str):
    instructions =  st.split("\n")  
    for instruction in instructions:
        instructStr = instruction.split()
        match(instructStr[0]):
            case "LET":
                createVariable(instructStr)
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
st = "LET INT x BE 5\nLET FLOAT y BE 10\nADD x TO y"
main(st)