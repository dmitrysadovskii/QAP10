from abc import ABC, abstractmethod


class Methods(ABC):
    @abstractmethod
    def addition(self):
        raise NotImplementedError

    @abstractmethod
    def subtraction(self):
        raise NotImplementedError

    @abstractmethod
    def multiplication(self):
        raise NotImplementedError

    @abstractmethod
    def division(self):
        raise NotImplementedError


class Calculator(Methods):
    def __init__(self, num_1, num_2):
        assert isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)), TypeError(
            "Variables should be defined as an integer or float")

        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        return self.num_1 + self.num_2

    def subtraction(self):
        return self.num_1 - self.num_2

    def multiplication(self):
        return self.num_1 * self.num_2

    def division(self):
        assert self.num_2 != 0, ZeroDivisionError('Divisor cannot be zero')
        return self.num_1 / self.num_2
