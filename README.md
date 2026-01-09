# Interactive Calculator

A small, user-friendly command-line calculator implemented in Python. The script prompts the user for two numbers and an operation, validates input with re-prompts until valid values are provided, performs the calculation, and prints the result.

This README documents usage, behavior, examples, and suggestions for improvements.

## Features

- Interactive prompts for two numbers and an operation.
- Robust input validation using while loops (re-prompts until valid input is entered).
- Supported operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Division-by-zero handling with a clear error message.

## Requirements

- Python 3.7 or newer

(If you need to install Python, visit the official site: [python.org](https://www.python.org/).)

## Installation

No installation is required. Save the script to a file (for example, `calculator.py`) and run it with Python.

## Usage

Run the script from a terminal:

```bash
python calculator.py
```

The program prompts for the first number, the operation, and the second number. It will keep prompting until the user provides valid inputs.

Example interactive session:

```
$ python calculator.py
Enter the first number: 12.5
Enter the operation (+, -, *, /): /
Enter the second number: 2
The result of 12.5 / 2.0 is: 6.25
```

If a user enters invalid input, the script explains the problem and asks again:

```
Enter the first number: twelve
Invalid input. Please enter a valid number.
Enter the first number: 12
Enter the operation (+, -, *, /): x
Invalid operation. Please enter one of +, -, *, /.
Enter the operation (+, -, *, /): +
Enter the second number: 0
The result of 12.0 + 0.0 is: 12.0
```

If division is attempted with a second number equal to zero, the script prints an error message and exits:

```
Enter the first number: 10
Enter the operation (+, -, *, /): /
Enter the second number: 0
Error: Division by zero is not allowed.
```

## How it works (brief)

- Each prompt is wrapped in a `while True` loop so the program can re-prompt when an invalid value is provided.
- Numeric input is converted to `float` inside a `try/except` block to catch invalid numeric entries.
- The operation is validated by checking membership in `['+', '-', '*', '/']`.
- Division includes an explicit check against `0` for safe handling of division-by-zero.

## Example script (concept)

Your current script structure looks like this (saved as `calculator.py`):

```python
# Prompt user for first number 
while True:
    first_number = input("Enter the first number: ")
    try:
        first_number = float(first_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompt user for operation
while True:
    operation = input("Enter the operation (+, -, *, /): ")
    if operation in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Prompt user for second number
while True:
    second_number = input("Enter the second number: ")
    try:
        second_number = float(second_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Perform calculation and print result (includes division-by-zero check)
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = first_number / second_number

print(f"The result of {first_number} {operation} {second_number} is: {result}")
```

## AI Collaboration Log
I used an AI assistant to help refactor and improve the script's input validation and user interaction. The AI suggested replacing the one-shot prompts and immediate exit() calls with while loops that re-prompt until valid input is provided, improving robustness and user experience. The AI also helped polish messaging and suggested further enhancements (command-line arguments, tests, etc.).

Prompt used (verbatim):
```
This code works great, the only thing I want fixed is instead of exit() after an invalid input, I want to prompt the user again. It needs to do so until a valid input has been accepted. Do it for all three prompts
```

This was the AI's response back
```
Now I'll modify the code to use while loops for all three prompts so the user gets re-prompted until valid input is provided:

Edited
calculator.py+25-21

Done! All three prompts now use while loops that keep asking for input until valid data is provided, instead of exiting on invalid
```

## Suggestions & Possible Enhancements

- Allow an exit command like `q` or `quit` at each prompt.
- Add command-line argument support (e.g., `python calculator.py 3 + 4`) using `argparse`.
- Add formatting options for the result (number of decimal places).
- Add unit tests for the calculation logic (separate pure functions for operations).
- Expand supported operations (exponentiation, modulo, parentheses, etc.).
- Add logging or a verbose mode for debugging.

## Contributing

Contributions and improvements are welcome. Please open an issue or submit a pull request with a clear description of the change.

## Author

nathan-hammond-uvu
