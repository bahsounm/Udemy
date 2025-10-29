# Calculator
import operations as op

# result = 0
# nxt_stp = 'n'

# while True:
#     if nxt_stp == 'n':
#         x = float(input("What is the first number?: "))
#         operation = input("+\n-\n*\n/\nPick an operation: ")
#         y = float(input("What is the next number?: "))
#         result = 0
#     else:
#         x = result
#         operation = input("+\n-\n*\n/\nPick an operation: ")
#         y = float(input("What is the next number?: "))

#     if operation == "+":
#         result = op.add(x,y)
#     elif operation == "-":
#         result = op.sub(x,y)
#     elif operation == "*":
#         result = op.multiply(x,y)
#     elif operation == "/":
#         result = op.divide(x,y)

#     print(f"{x} {operation} {y} = {result}")

#     nxt_stp = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
#     if nxt_stp not in ['y', 'n']:
#         break


#---------------------------------------------------------------------------------
# simplified

operation_map = {
    "+": op.add,
    "-": op.sub,
    "*": op.multiply,
    "/": op.divide,
}

def calc():
    result = None

    while True:
        if result is None:
            x = float(input("What is the first number?: "))
        else:
            x = result

        operation = input("+\n-\n*\n/\nPick an operation: ")
        y = float(input("What is the next number?: "))

        if operation in operation_map:
            result = operation_map[operation](x, y)
            print(f"{x} {operation} {y} = {result}")
        else:
            print("Invalid operation")
            continue

        nxt_stp = input(f"Type 'y' to continue with {result}, or 'n' for new calculation: ").lower()
        if nxt_stp == "n":
            result = None
        elif nxt_stp != "y":
            break

calc()