# Dictionary to store variables as key value pairs
variables = {}

# Function to extract value
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
        return 0 # Fallback

# Function to create a variable : value pair
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

# Function to assign value to a variable
def setVariable(instruction):
    var = instruction[1]
    val = getValue(instruction[3])
    variables[var] = val

# ---- Arithmetic Operations ---- 
def addInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    variables[var] += val
    
def subInstruct(instruction):
    val = getValue(instruction[1])
    var = instruction[3]
    variables[var] -= val
    
def mulInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    variables[var] *= val

def remInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    variables[var] %= val

def divInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    variables[var] /= val

def expInstruct(instruction):
    val = getValue(instruction[3])
    var = instruction[1]
    variables[var] **= val
# ---- ---- --- --- --- ---- ----

# --- I/O operations ---
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
# --- ---- ---- ---- ---

def evalCondition(instruction:list[str])->bool:
    arg1 = getValue(instruction[1])
    op = instruction[2]
    arg2 = getValue(instruction[3])
    flag = False
    match op:
        case "EQ": flag = arg1 == arg2
        case "NE": flag = arg1 != arg2
        case "LT": flag = arg1 < arg2  
        case "GT": flag = arg1 > arg2  
        case "LE": flag = arg1 <= arg2
        case "GE": flag = arg1 >= arg2
    return flag

# --- Helper function for conditional statements ---
def find_next_branch(instructions, start_index, max_len):
    i = start_index
    nesting = 0
    while i < max_len:
        parts = instructions[i].split()
        if not parts: 
            i += 1
            continue
            
        cmd = parts[0]
        if cmd == "IF":
            nesting += 1
        elif cmd == "ENDIF":
            if nesting == 0:
                return i, "ENDIF"
            nesting -= 1
        elif nesting == 0:
            if cmd == "ELSE":
                return i, "ELSE"
            elif cmd == "ELIF":
                return i, "ELIF"
        i += 1
    return max_len, "EOF"

# Main function
def main(st:str):
    instructions = st.split("\n")
    n = len(instructions)
    instPtr = 0  
    loopStack = [] # Stack to keep track of WHILE loops
    
    while(instPtr < n):
        instructStr = instructions[instPtr].split()
        if len(instructStr) == 0:
            instPtr += 1
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
            
            # --- Conditional Logic ---
            case "IF":
                flag = evalCondition(instructStr)
                if flag:
                    pass # Just fall through and execute inside
                else:
                    current_idx = instPtr + 1
                    found_branch = False
                    
                    while not found_branch:
                        idx, type = find_next_branch(instructions, current_idx, n)
                        
                        if type == "ENDIF" or type == "ELSE":
                            instPtr = idx
                            found_branch = True
                        elif type == "ELIF":
                            elif_parts = instructions[idx].split()
                            elif_flag = evalCondition(elif_parts)
                            if elif_flag:
                                instPtr = idx
                                found_branch = True
                            else:
                                current_idx = idx + 1
                        else:
                            instPtr = n # EOF
                            found_branch = True

            case "ELSE" | "ELIF":
                # If we hit this naturally, a previous block succeeded. Skip to ENDIF
                current_idx = instPtr + 1
                while True:
                    idx, type = find_next_branch(instructions, current_idx, n)
                    if type == "ENDIF" or type == "EOF":
                        instPtr = idx
                        break
                    current_idx = idx + 1

            # --- While loop logic ---
            case "WHILE":
                flag = evalCondition(instructStr)
                if flag:
                    loopStack.append(instPtr) # Save line to return to
                else:
                    whileCounter = 1
                    while whileCounter > 0:
                        instPtr += 1
                        if instPtr >= n:
                            print("ERROR: Missing ENDWHILE")
                            return
                        skim_line = instructions[instPtr].split()
                        if len(skim_line) == 0:
                            continue
                        if skim_line[0] == "WHILE":
                            whileCounter += 1
                        elif skim_line[0] == "ENDWHILE":
                            whileCounter -= 1
            
            case "ENDWHILE":
                if len(loopStack) > 0:
                    return_line = loopStack.pop()
                    instPtr = return_line - 1 # Jump back up
                else:
                    print("ERROR: ENDWHILE found without active WHILE")
                    
        instPtr += 1

# --- Driver Code ---
if __name__ == "__main__":
    # Test Script
    st = """
    LET INT x BE 0

    OUTPUT "--- Testing WHILE Loop ---"
    WHILE x LT 3
        ADD 1 TO x
        OUTPUT x
    ENDWHILE

    OUTPUT "--- Testing IF / ELIF / ELSE ---"
    IF x EQ 100
        OUTPUT "x is 100 (Failed)"
    ELIF x EQ 3
        OUTPUT "x is exactly 3 (Success!)"
    ELSE
        OUTPUT "x is something else (Failed)"
    ENDIF
    """
    main(st)