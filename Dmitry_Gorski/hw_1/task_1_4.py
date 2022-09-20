def func_mean_1(a: int, b: int) -> float:
    """Функция для определения среднего арифметического 2-х натуральных чисел"""
    return float((a + b) / 2)


def func_mean_2(a: int, b: int) -> float:
    """Функция для определения среднего геометрического 2-х натуральных чисел"""
    return float(abs(a * b) ** .5)


x, y = 10, 20
print('Cреднее арифметическое :', func_mean_1(x, y))
print('Cреднее геометрическое :', func_mean_2(x, y))
