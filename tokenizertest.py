import re

def tokenize(code_string): 
    pattern = r"""
        "[^"]*"       | # Match Strings first (e.g., "Hello World")
        \d+\.\d+      | # Match Floats next (e.g., 10.5)
        \d+           | # Match Integers (e.g., 42)
        [A-Za-z_]+    | # Match Words (e.g., SET, x, IF)
        [+\-*/<>=()]    # Match Math/Logic Symbols
    """
    
    # re.VERBOSE allows us to write the pattern on multiple lines with comments
    # re.findall scans the string and returns a list of EVERYTHING that matches.
    tokens = re.findall(pattern, code_string, re.VERBOSE)
    
    return tokens

# --- Testing ---

# Test 1: Breaking point
print("Test 1:", tokenize("SET X TO 67/100"))
# Output: ['SET', 'X', 'TO', '67', '/', '100']

# Test 2: Complex Math (Shunting Yard)
print("Test 2:", tokenize("IF (x + 5) * 10 GT 50"))
# Output: ['IF', '(', 'x', '+', '5', ')', '*', '10', 'GT', '50']

# Test 3: Strings with spaces
print("Test 3:", tokenize('LET STR msg BE "Hello World"'))
# Output: ['LET', 'STR', 'msg', 'BE', '"Hello World"']