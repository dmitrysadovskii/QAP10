from func import Methods


class Calculator(Methods):

    @staticmethod
    def validation(number1, number2):
        if not isinstance(number1, (int, float)):
            raise print("Numbers should be integer or float")
        elif not isinstance(number2, (int, float)):
            raise print("Numbers should be integer or float")

    def addition(self, number1, number2):
        self.validation(number1, number2)
        return print(f"Your addition result: {number1 + number2}")

    def subtraction(self, number1, number2):
        self.validation(number1, number2)
        return print(f"Your subtraction result: {number1 - number2}")

    def multiplication(self, number1, number2):
        self.validation(number1, number2)
        return print(f"Your multiplication result: {number1 * number2}")

    def division(self, number1, number2):
        self.validation(number1, number2)
        if int(number2) == 0:
            raise ZeroDivisionError("Please enter number not equal to zero")
        return print(f"Your division result: {number1 / number2}")


calc = Calculator()
calc.addition(20, 13)
calc.division(20, 4.5)
calc.subtraction(5, 3.3)
calc.multiplication(2.2, 8)
