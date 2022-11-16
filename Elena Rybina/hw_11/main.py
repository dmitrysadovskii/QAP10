from func import Methods


class Calculate(Methods):

    def addition(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Enter numbers can be integer or float!'
        assert isinstance(num_2, (float, int)), 'Enter numbers can be integer or float!'
        return num_1 + num_2

    def subtraction(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Enter numbers can be integer or float!'
        assert isinstance(num_2, (float, int)), 'Enter numbers can be integer or float!'
        return num_1 - num_2

    def multiplication(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Enter numbers can be integer or float!'
        assert isinstance(num_2, (float, int)), 'Enter numbers can be integer or float!'
        return num_1 * num_2

    def division(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Enter numbers can be integer or float!'
        assert isinstance(num_2, (float, int)), 'Enter numbers can be integer or float!'
        assert num_2 != 0, 'Division by zero!'
        return num_1 / num_2


calculator = Calculate()

print(calculator.addition(53, 36))
print(calculator.subtraction(85, 0.3))
print(calculator.multiplication(1.5, 2))
print(calculator.division(1.989, 17))
