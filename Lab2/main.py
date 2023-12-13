class Calculator:
    def __init__(self):
        self.result = None

    def get_user_input(self):
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /, ^, √, %): ")
            num2 = float(input("Enter the second number: "))
            return num1, operator, num2
        except ValueError:
            print("Invalid number format. Try again.")
            return self.get_user_input()

    def check_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        if operator not in valid_operators:
            print("Error: Invalid operator entered. Please enter a valid operator.")
            return False
        return True

    def calculate(self, num1, operator, num2):
        if operator == '+':
            self.result = num1 + num2
        elif operator == '-':
            self.result = num1 - num2
        elif operator == '*':
            self.result = num1 * num2
        elif operator == '/':
            try:
                self.result = num1 / num2
            except ZeroDivisionError:
                print("You cannot divide by zero!")
        elif operator == '^':
            self.result = num1 ** num2
        elif operator == '√':
            self.result = num1 ** 0.5
        elif operator == '%':
            self.result = num1 % num2

    def run_calculator(self):
        memoryres = []
        decimal_places = 2  
        while True:
            num1, operator, num2 = self.get_user_input()
            if self.check_operator(operator):
                self.calculate(num1, operator, num2)
                if self.result is not None:
                    print(f"Answer: {self.result:.{decimal_places}f}")

            archive1 = input("Do you want to save the result to the archive? (yes/no): ")
            if archive1.lower() == 'yes':
                memoryres.append(self.result)
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

class ScientificCalculator(Calculator):
    def calculate(self, num1, operator, num2):
        if operator == '√':
            self.result = num1 ** (1 / num2)
        else:
            super().calculate(num1, operator, num2)

def main():
    print("Welcome to the Calculator!")
    calculator = ScientificCalculator()
    calculator.run_calculator()

if __name__ == "__main__":
    main()
                    
          
