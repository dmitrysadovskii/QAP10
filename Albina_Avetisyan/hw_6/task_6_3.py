import sys


def add_up_the_number(number1, number2: int) -> int:
    return number1 + number2


def multiply(number1, number2: int) -> int:
    return number1 * number2


def subtract(number1, number2: int) -> int:
    return number1 - number2


def divide(number1, number2: int) -> tuple:
    try:
        unit = number1 // number2
        fractional = number1 % number2
        return unit, fractional
    except ZeroDivisionError:
        print('ОШИБКА! Замените второе число!')
        sys.exit()


print('Выбирите операцию:\n'
      '1.Сложение\n'
      '2.Вычитание\n'
      '3.Умножение\n'
      '4.Деление\n')
choice = int(input('Введите номер операции: '))
if 1 >= choice or choice <= 4:
    pass
else:
    print('ОШИБКА! Выберите номер операции из предложенных!')
    sys.exit()
number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
if choice == 1:
    print(add_up_the_number(number_1, number_2))
elif choice == 2:
    print(subtract(number_1, number_2))
elif choice == 3:
    print(multiply(number_1, number_2))
elif choice == 4:
    result = divide(number_1, number_2)
    print(f"Частное: {result[0]}, Остаток: {result[1]}")
