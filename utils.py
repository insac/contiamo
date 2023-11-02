# Define the set of numbers
number_set = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 200]


# Define a function to perform algebraic operations
def perform_operation(a, b, operation):
    if operation == '+':
        if a + b < 10000:
            return a + b
    elif operation == '-':
        if a - b >= 0:
            return a - b
    elif operation == '*':
        if a * b < 10000:
            return a * b
    elif operation == '/':
        if b != 0 and a % b == 0:
            return int(a / b)
    return None

