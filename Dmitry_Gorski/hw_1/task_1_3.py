def cube_square(a: float) -> float:
    """Функция расчета площади грани куба"""
    return float(a ** 2)


def cube_size(a: float) -> float:
    """Функция расчета объема куба"""
    return float(cube_square(a) * a)


x = 50
print('Площадь грани куба :', cube_square(x))
print('Объем куба :', cube_size(x))
