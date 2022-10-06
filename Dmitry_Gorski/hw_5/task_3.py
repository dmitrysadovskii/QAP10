while True:
    user_number = input('Input 4-digit number (numbers must not be repeated): ')
    secret_number, cows_bulls_counter = '3219', {'Cows': 0, 'Bulls': 0}
    try:
        assert user_number.isdigit() and len(list(set(user_number))) == 4, print('Attention!!!\n')
        for i in list(user_number):
            if i in list(secret_number):
                if list(user_number).index(i) == list(secret_number).index(i):
                    cows_bulls_counter['Bulls'] = int(cows_bulls_counter.get('Bulls')) + 1
                else:
                    cows_bulls_counter['Cows'] = int(cows_bulls_counter.get('Cows')) + 1
                if int(cows_bulls_counter.get('Bulls')) == 4:
                    print('You win!!!')
                    exit(0)
        print(f'Bulls -- {cows_bulls_counter.get("Bulls")}, Cows -- {cows_bulls_counter.get("Cows")}\n')
    except AssertionError:
        continue
