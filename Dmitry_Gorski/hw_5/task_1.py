import re


def install_lang(lst: list) -> str:
    return 'eng' if re.match('[a-zA-Z]', ''.join(lst)) == 'eng' else None


def likes(lst: list) -> str:
    if len(lst) == 0:
        return 'Никому не нравится / No one likes this'
    if len(lst) == 1:
        return '{} нравится это'.format(*lst) if install_lang(lst) \
            else '{} likes this'.format(*lst)
    if len(lst) == 2:
        return '{} и {} нравится это'.format(*lst) if install_lang(lst) \
            else '{} and {} like this'.format(*lst)
    if len(lst) == 3:
        return '{}, {} и {} нравится это'.format(*lst) if install_lang(lst) \
            else '{}, {} and {} like this'.format(*lst)
    else:
        return '{}, {} и'.format(*lst) + f'{len(lst) - 2} остальным нравится это' if install_lang(lst) \
            else '{}, {} and'.format(*lst) + f'{len(lst) - 2} others like this'


print(likes([]))
print(likes(['Ann']))
print(likes(['Ann', 'Alex']))
print(likes(['Ann', 'Alex', 'Mark']))
print(likes(['Ann', 'Alex', 'Mark', 'Max']))
