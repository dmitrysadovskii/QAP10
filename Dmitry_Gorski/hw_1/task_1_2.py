def formula(x: int, y: int) -> float:
    """Функция для расчета формулы"""
    return (abs(x) - abs(y)) / 1 + abs(x * y)


a, b = 500, -500
print('Результат :', formula(a, b))
