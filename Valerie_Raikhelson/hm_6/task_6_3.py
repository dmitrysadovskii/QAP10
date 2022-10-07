op = input("Выберите операцию:"
           "\n1. Сложение"
           "\n2. Вычитание"
           "\n3. Умножение"
           "\n4. Деление "
           "    \nВведите номер пункта меню:")


def num_1():
    return float(input("Введите первое число:"))


def num_2():
    return float(input("Введите второе число:"))


if op == "1":
    print(num_1() + num_2())
elif op == "2":
    print(num_1() - num_2())
elif op == "3":
    print(num_1() * num_2())
elif op == "4":
    try:
        print(num_1() / num_2())
    except ZeroDivisionError:
        print("Invalid operator")
