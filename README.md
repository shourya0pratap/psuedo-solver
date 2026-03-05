# Custom Pseudocode Interpreter

A lightweight, fully-functional interpreter for a custom, English-like Domain Specific Language (DSL), written entirely in Python. 

This project bridges the gap between natural language pseudocode and executable logic, making it an excellent tool for learning programming fundamentals, algorithm design, and compiler architecture.

## 🚀 Features

* **English-like Syntax:** Designed to be highly readable (e.g., `ADD 5 TO x` instead of `x += 5`).
* **Turing Complete:** Full support for conditional branching (`IF`/`ELIF`/`ELSE`) and iterative loops (`WHILE`).
* **Strongly Typed Declarations:** Supports `INT`, `FLOAT`, `STR`, and `BOOL`.
* **Custom Lexical Scanner:** Built-in Regex tokenizer for precise code parsing.
* **Expression Evaluation:** (WIP) Shunting Yard algorithm integration for standard algebraic math expressions.

## 🧠 Architecture

The interpreter operates in a multi-stage pipeline:
1.  **Lexer/Tokenizer:** Reads the raw string input and categorizes text into machine-readable tuples (Keywords, Identifiers, Numbers, Symbols).
2.  **Instruction Pointer (IP) Engine:** A state-machine main loop that dictates control flow, capable of skipping lines (for failed conditions) or jumping backwards (for loops).
3.  **Global Symbol Table:** A dictionary-based memory manager that tracks variable states during runtime.
4.  **Expression Evaluator:** Converts Infix math expressions to Postfix using the Shunting Yard algorithm for accurate order-of-operations computation.

## 🛠️ Quick Start

**Prerequisites:** Python 3.10+

1. Clone this repository.
2. Open `main.py` (or your script name).
3. Write your custom code inside the `st` string variable.
4. Run the script:
```bash
python main.py