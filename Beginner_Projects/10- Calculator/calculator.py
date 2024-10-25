from art import logo

new_input = True
first_number = None

def first_num():
    global first_number
    while type(first_number) != int:
        if first_number is None:
            first_number = input("What's the first number?: ")
        elif type(first_number) is not int:
            first_number = input("Please write a number.\nWhat's the first number?: ")
        try:
            first_number = int(first_number)
        finally:
            continue
    return first_number

def make_the_operation(operation_math, n1, n2):
    return eval(str(n1) + operation_math + str(n2))
while True:
    if new_input:
        print("\n" * 100)
        print(logo)
    first_num()
    operation = input("+\n-\n*\n/\nPick an operation: ")
    operation_valid = True
    while not operation_valid:
        if operation != "+" or "-" or "*" or "/":
            operation = input("You didn't pick an operation\n+\n-\n*\n/\nPick an operation: ")
        else:
            operation_valid = True
    second_number = input("What's the second number?: ")
    second_number_valid = False
    while not second_number_valid:
        try:
            second_number = int(second_number)
            second_number_valid = True
        except ValueError:
            second_number = input("Please write a number.\nWhat's the second number?: ")
    output = make_the_operation(operation, first_number, second_number)
    print(f"{first_number} {operation} {second_number} = "
          f"{output}")
    is_going = input("Type 'y' to continue calculating with 6.0, or type 'n' to start a new calculation: ")
    if is_going == "y":
        first_number = int(output)
        new_input = False
    else:
        first_number = None
        new_input = True

