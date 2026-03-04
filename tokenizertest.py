import re

# Set of all keywords
KEYWORDS = {
    "LET", "INT", "FLOAT", "STR", "BOOL", "BE", "SET", "TO", 
    "ADD", "SUB", "FROM", "MUL", "WITH", "DIV", "BY", "EXP", "REM", 
    "INPUT", "AS", "OUTPUT", "PRINT", 
    "IF", "ELSE", "ELIF", "ENDIF", "WHILE", "ENDWHILE", 
    "EQ", "NE", "LT", "GT", "LE", "GE", "AND", "OR", "NOT"
}

def tokenize(code_string):
    # 1. EXTRACT
    pattern = r"""
        "[^"]*"       | # Match Strings
        \d+\.\d+      | # Match Floats
        \d+           | # Match Integers
        [A-Za-z_]\w* | # Match Words (Keywords or Identifiers)
        [+\-*/<>=()]    # Match Symbols
    """
    raw_tokens = re.findall(pattern, code_string, re.VERBOSE)
    
    categorized_tokens = []
    
    # 2. CATEGORIZE
    for token in raw_tokens:
        first_char = token[0]
        
        if first_char.isalpha() or first_char == "_":
            # Keyword or a Variable
            if token in KEYWORDS:
                categorized_tokens.append(("KEYWORD", token))
            else:
                categorized_tokens.append(("IDENTIFIER", token))
                
        elif first_char.isdigit():
            # Number
            categorized_tokens.append(("NUMBER", token))
            
        elif first_char == '"':
            # String Literal
            categorized_tokens.append(("STRING", token.strip('"')))
            
        else:
            # If it's none of the above, it's a Math/Logic Symbol
            categorized_tokens.append(("SYMBOL", token))
            
    return categorized_tokens

# --- Test ---
test_code = 'SET var1 TO (67 + y) / 100'
tokens = tokenize(test_code)

for t in tokens:
    print(t)