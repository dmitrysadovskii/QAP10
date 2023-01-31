print("Выберите операцию:\n"
      "1. Сложение\n"
      "2. Вычитание\n"
      "3. Умножение\n"
      "4. Деление")

ask_operation = int(input('Введите номер пункта меню:'))
first_number = int(input('Введите первое число:'))
second_number = int(input('Введите второе число:'))


def operation():
    if ask_operation == 1:
        print(f'Сумма чисел равна {first_number + second_number}')
    if ask_operation == 2:
        print(f'Разность чисел равна {first_number - second_number}')
    if ask_operation == 3:
        print(f'Произведение чисел равно {first_number * second_number}')
    if ask_operation == 4:
        if second_number == 0:
            print('Деление на ноль запрещено')
        else:
            print(f'Частное от деления равно {first_number // second_number}' 
                  f'остаток от деления {first_number % second_number}')


operation()
