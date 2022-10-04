secret_number = '3219'

while True:
    user_number = input('Введите 4-х значное число (цифры не должны повторяться): ')
    d = {'Бык(и)': 0, 'Корова(ы)': 0}
    if user_number.isdigit() and len(list(set(user_number))) == 4:
        for i in list(user_number):
            if i in list(secret_number):
                d['Корова(ы)'] = int(d.get('Корова(ы)')) + 1
                if list(user_number).index(i) == list(secret_number).index(i):
                    d['Бык(и)'] = int(d.get('Бык(и)')) + 1
                    if int(d.get('Бык(и)')) == 4:
                        print('Вы выиграли !!!')
                        exit(0)
        print(f'Увы, но пока Быков -- {d.get("Бык(и)")}, а Коров -- {d.get("Корова(ы)")}\n')
    else:
        print('Обратите внимание на условие ввода!!!\n')
        continue
