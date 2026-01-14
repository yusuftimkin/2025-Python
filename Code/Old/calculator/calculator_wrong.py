def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def calculator ():
    n1 =int(input("Enter a number: "))
    operation = input("Enter a operation: ")
    n2 =int(input("Enter another number: "))

    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        return None

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate_result():
    n1 = result
    operation = input("Enter a operation: ")
    n2 = int(input("Enter another number: "))

    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        return None

continue_calculate = True

while continue_calculate:
    print(calculator())
    ask_continue = input("Do you want to continue? (y/n): ").lower()
    result = calculator()

    if ask_continue == "y":
        print(calculate_result())
    else:
        continue_calculate = False
        print(calculator())