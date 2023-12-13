import math

memoryres = []
decimal_places = 0

while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, ^, √, %): ")

    if operator not in ('+', '-', '*', '/', '^', '√', '%'):
        print("Error: Invalid operator entered. Please enter a valid operator.")
        continue

    num2 = float(input("Enter the second number: "))

    # Питаємо користувача про кількість десяткових розрядів тільки один раз
    if decimal_places == 0:
        decimal_places = int(input("Enter the number of decimal places to display: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("You cannot divide by zero!")
            continue
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '^':
        result = num1 ** num2
    elif operator == '√':
        if num1 < 0:
            print("The operation is impossible! ")
            continue
        result = math.sqrt(num1)

    print(f"Answer: {result:.{decimal_places}f}")

    povtor = input("Would you like to repeat (yes/no)?")
    if povtor.lower() != "yes":
        # Решта коду для збереження, відновлення, налаштування і т.д.
        
        archive1 = input("Do you want to save the result to the archive? (yes/no): ")
        if archive1.lower() == 'yes':
            memoryres.append(result)
            print("The result is saved in the archive")

        archive2 = input("Do you want to restore the archive? (yes/no): ")
        if archive2.lower() == 'yes':
            if memoryres:
                print("Archive of saved results:")
                for i, saved_result in enumerate(memoryres, start=1):
                    print(f"{i}. {saved_result:.{decimal_places}f}")
            else:
                print("The archive is empty!")

        magazine = input("Open the magazine? (yes/no): ")
        if magazine.lower() == 'yes':
            if memoryres:
                print("Magazine:")
                for i, saved_result in enumerate(memoryres, start=1):
                    print(f"{i}. Result: {saved_result:.{decimal_places}f}")
            else:
                print("The magazine is empty!")

        settings = input("Do you want to configure calculator settings? (yes/no): ")
        if settings.lower() == 'yes':
            decimal_places = int(input("Enter the number of decimal places to display: "))

        povtor = input("Do you want to make a new calculation? (yes/no): ")
        if povtor.lower() != 'yes':
            break
