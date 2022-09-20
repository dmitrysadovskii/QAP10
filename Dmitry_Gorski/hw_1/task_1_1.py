def summa(a: int, b: int) -> int:
    """Функция для определения суммы 2-х натуральных чисел"""
    return a + b


def diff(a: int, b: int) -> int:
    """Функция для определения разности 2-х натуральных чисел"""
    return a - b


def multiplication(a: int, b: int) -> int:
    """Функция для определения произведения 2-х натуральных чисел"""
    return a * b


x, y = 10, 50
print(f'Сумма чисел {x} и {y}:', summa(x, y))
print(f'Разность чисел {x} и {y}:', diff(x, y))
print(f'Произведение чисел {x} и {y}:', multiplication(x, y))
