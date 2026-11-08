
try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    operation = input("Choose an operation (+, -, *, /, %): ")

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            result = None
    elif operation == '%':
        if second_number  == 0:
            print("Error: division by zero")               
        else:
            result = first_number % second_number
    else:
        print("Invalid operation.")
        result = None

    if result is not None:
        print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter numbers.")
