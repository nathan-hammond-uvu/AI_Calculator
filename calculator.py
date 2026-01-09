# Prompt user for first number 
while True:
    first_number = input("Enter the first number: ")
    
    # validate response 
    try:
        first_number = float(first_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompt user for operation
while True:
    operation = input("Enter the operation (+, -, *, /): ")
    # validate operation
    if operation in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Prompt user for second number
while True:
    second_number = input("Enter the second number: ")
    
    # validate response
    try:
        second_number = float(second_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Perform calculation based on operation
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

# Display result
print(f"The result of {first_number} {operation} {second_number} is: {result}") 
