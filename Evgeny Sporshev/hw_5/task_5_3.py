secret_number = input('Игрок 1, загадай четырехзначное число число: ')


while True:
    suggested_number = input('Игрок 2, угадай четырехзначное число число: ')
    cow_counter = 0
    bull_counter = 0
    if suggested_number == secret_number:
        print('Вы выиграли!')
        break
    for i in range(len(suggested_number)):
        if suggested_number[i] == secret_number[i]:
            bull_counter += 1
        elif suggested_number[i] in secret_number:
            cow_counter +=1
        else:
            continue
    print('Коров:', cow_counter, 'Быков:', bull_counter)
