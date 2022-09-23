S = 'www.my_site.com#about'
print(S.replace('#', '/'))


def add_ing(s: str) -> str:
    return ' '.join([f'{i}ing' for i in s.split(' ')])


S = 'Ivanov Ivan'
print(' '.join(S.split(' ')[::-1]))


def del_space(s: str) -> str:
    return s.strip()
