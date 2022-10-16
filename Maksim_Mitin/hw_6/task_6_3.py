def calc():
    operation_number = int(input('Выберите операцию:\n1. Сложение\n2. Вычитание\n3.'
                                 ' Умножение\n4. Деление\n  Введите номер пункта меню:\n'))

    number_one = int(input('Введите первое число:\n'))
    number_two = int(input('Введите второе число:\n'))

    if operation_number == 1:
        result = number_one + number_two
        print(f'Результат сложения {result}')
    elif operation_number == 2:
        result = number_one - number_two
        print(f'Результат вычитания {result}')
    elif operation_number == 3:
        result = number_one * number_two
        print(f'Результат умножения {result}')
    elif operation_number == 4:
        if number_one or number_two == 0:
            print('Одно из значений равно 0, на ноль делить нельзя. Программа завершает работу')
        else:
            result = number_one / number_two
            print(f'Результат деления {result}')


calc()
