from func import Methods


class Calculator(Methods):
    def addition(self, num_1, num_2):
        try:
            return float(num_1) + float(num_2)
        except ValueError:
            return "Error: Invalid input"

    def subtraction(self, num_1, num_2):
        try:
            return float(num_1) - float(num_2)
        except ValueError:
            return "Error: Invalid input"

    def multiplication(self, num_1, num_2):
        try:
            return float(num_1) * float(num_2)
        except ValueError:
            return "Error: Invalid input"

    def division(self, num_1, num_2):
        try:
            return float(num_1) / float(num_2)
        except ValueError:
            return "Error: Invalid input"
        except ZeroDivisionError:
            return "Error: Division by zero"


def main():
    calculator = Calculator()
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '5':
            break

        num_1 = input("Enter first number: ")
        num_2 = input("Enter second number: ")

        if choice == '1':
            result = calculator.addition(num_1, num_2)
        elif choice == '2':
            result = calculator.subtraction(num_1, num_2)
        elif choice == '3':
            result = calculator.multiplication(num_1, num_2)
        elif choice == '4':
            result = calculator.division(num_1, num_2)
        else:
            result = "Error: Invalid input"

        print("Result:", result)


if __name__ == "__main__":
    main()
