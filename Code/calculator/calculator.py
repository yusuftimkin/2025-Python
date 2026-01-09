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

continue_calculate = True

while continue_calculate:
    print(calculator())
    ask_continue = input("Do you want to continue? (y/n): ").lower()

    if ask_continue == "y":
        continue_calculate = True
    else:
        continue_calculate = False

