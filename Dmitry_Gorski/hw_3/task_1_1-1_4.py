''' Заменить символ “#” на символ “/” в строке www.my_site.com#about '''
s = 'www.my_site.com#about'
print(s.replace('#', '/'))


''' Напишите программу, которая добавляет ing к словам '''
def add_ing(s: str) -> str:
    return ' '.join([ f'{i}ing' for i in s.split(' ')])


''' В строке Ivanou Ivan поменяйте местами слова Ivan Ivanou '''
s = 'Ivanov Ivan'
print(' '.join(s.split(' ')[::-1]))


''' Напишите программу которая удаляет пробел в начале, в конце строки '''
def del_space(s: str) -> str:
    return s.strip()
