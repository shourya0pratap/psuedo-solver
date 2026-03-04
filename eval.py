# Standard PEMDAS precedence
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3  # Assuming you add ^ to your regex symbols for EXP
}

def infix_to_postfix(tokens):
    output = []
    op_stack = []
    
    for token_type, value in tokens:
        # 1. Operands (Numbers and Variables) go straight to output
        if token_type in ("NUMBER", "IDENTIFIER", "STRING", "BOOL"):
            output.append((token_type, value))
            
        # 2. Operators and Parentheses
        elif token_type == "SYMBOL":
            if value == '(':
                op_stack.append(value)
            elif value == ')':
                # Pop until we find the matching '('
                while op_stack and op_stack[-1] != '(':
                    output.append(("SYMBOL", op_stack.pop()))
                op_stack.pop() # Discard the '('
            else:
                # It's a math operator (+, -, *, /)
                while (op_stack and op_stack[-1] != '(' and PRECEDENCE.get(op_stack[-1], 0) >= PRECEDENCE.get(value, 0)):
                    output.append(("SYMBOL", op_stack.pop()))
                op_stack.append(value)
                
    # 3. Pop remaining operators
    while op_stack:
        output.append(("SYMBOL", op_stack.pop()))
        
    return output