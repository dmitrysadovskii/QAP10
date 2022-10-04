while True:
    user_number = input('Input 4-digit number (numbers must not be repeated): ')
    secret_number, d = '3219', {'Cows': 0, 'Bulls': 0}
    try:
        assert user_number.isdigit() and len(list(set(user_number))) == 4, print('Attention!!!\n')
        for i in list(user_number):
            if i in list(secret_number):
                d['Cows'] = int(d.get('Cows')) + 1
                if list(user_number).index(i) == list(secret_number).index(i):
                    d['Bulls'] = int(d.get('Bulls')) + 1
                    if int(d.get('Bulls')) == 4:
                        print('You win!!!')
                        exit(0)
        print(f'Bulls -- {d.get("Bulls")}, Cows -- {d.get("Cows")}\n')
    except AssertionError:
        continue
