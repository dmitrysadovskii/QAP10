def calculate(number_1, number_2, operator):
    if not number_1.isdigit() or not number_2.isdigit():
        return 'Enter number!'
    if int(number_2) == 0 and operator == 'division':
        return 'Division by zero!'
    if operator not in ['addition', 'subtraction', 'multiplication', 'division']:
        return 'Enter correct operation!'
    if operator == 'addition':
        return int(number_1) + int(number_2)
    elif operator == 'subtraction':
        return int(number_1) - int(number_2)
    elif operator == 'multiplication':
        return int(number_1) * int(number_2)
    elif operator == 'division':
        return int(number_1) / int(number_2)


print(calculate((input('Enter your number 1: ')),
                (input('Enter your number 2: ')),
                input('Enter operation - addition, subtraction, multiplication or division: ')))
