import random
number_1 = ''.join(random.sample('12345678', 4))   # the secret number
print('HELP: the secret number is: ', number_1)
cows = 0
bulls = 0
while True:
    number_2 = input('Please enter four-digit number with non-repetitive digits: ', )  # try to guess
    print('yor\'s number: ', number_2)
    if int(number_2) == int(number_1):
        print('You won!')
        break

    elif len(number_2) != 4:
        print('Error! Your\'s number is tot four-digit. Enter four-digit number!')

    elif abs(int(number_2)) == 0:
        print('Error! Enter four-digit non-zero number!')

    # elif number_2 == '':
    #   print('Error! Enter four-digit number!')
    # не удалось задать условие возврата к началу при вводе пустого значения!

    else:

        for i in list(str(number_1)):
            for i2 in list(str(number_2)):
                if i == i2:
                    cows += 1

        if str(number_1)[0] == str(number_2)[0]:
            bulls += 1
        if str(number_1)[1] == str(number_2)[1]:
            bulls += 1
        if str(number_1)[2] == str(number_2)[2]:
            bulls += 1
        if str(number_1)[3] == str(number_2)[3]:
            bulls += 1

        print("cows: ", cows)
        print("bulls: ", bulls)
