def rectangle_cathetus(a: float, b: float) -> float:
    """Функция расчета катета прямоугольного треугольника"""
    return float((a ** 2 + b ** 2) ** .5)


def rectangle_size(a: float, b: float) -> float:
    """Функция расчета площади прямоугольного треугольника"""
    return float((a * b) / 2)


x, y = 3, 4
print('Площадь грани куба :', rectangle_cathetus(x, y))
print('Объем куба :', rectangle_size(x, y))
