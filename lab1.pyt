import math

memory = None
calculation_history = []
precision = 2  

def perform_calculation(num1, num2, operator):
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Error! Division by zero.")
        result = num1 / num2
    elif operator == '^':
        result = num1 ** num2
    elif operator == '√':
        if num1 < 0:
            raise ValueError("Error! Cannot calculate the square root of a negative number.")
        result = math.sqrt(num1)
    elif operator == '%':
        result = num1 % num2
    return result

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        while True:
            operator = input("Enter an operator (+, -, *, /, ^ for exponentiation, √ for square root, % for remainder, M to save to memory, R to recall memory, H to view history, S to change settings): ")
            if operator in ('+', '-', '*', '/', '^', '√', '%', 'M', 'R', 'H', 'S'):
                break
            else:
                print("Error! Invalid operator. Please enter a valid operator.")

        if operator == 'M':
            memory = result
            print("Result saved to memory.")
        elif operator == 'R':
            if memory is not None:
                print("Memory value:", memory)
            else:
                print("Memory is empty.")
        elif operator == 'H':
            if not calculation_history:
                print("Calculation history is empty.")
            else:
                print("Calculation History:")
                for expr, result in calculation_history:
                    print(f"{expr} = {result}")
        elif operator == 'S':
            precision = int(input("Enter the number of decimal places to display: "))
        else:
            result = perform_calculation(num1, num2, operator)
            if result is not None:
                calculation_history.append((f"{num1} {operator} {num2}", result))
                print(f"Result: {result:.{precision}f}")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break