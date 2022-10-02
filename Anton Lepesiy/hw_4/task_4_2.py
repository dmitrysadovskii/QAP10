
spis1 = ['Ivan', 'Ivanou']
str1 = 'Minsk'
str2 = 'Belsrus'

a =' '.join(spis1)  # преобразование списка в строку

print('Привет,' + a +'! '+ 'Добро пожаловать в ' + str1 + ' ' + str2)

    # this metod don't working:
    # print('Привет, {name}! Добро пожаловать в {sity} {country}'.format(name=a, city=str1, country=str2))

