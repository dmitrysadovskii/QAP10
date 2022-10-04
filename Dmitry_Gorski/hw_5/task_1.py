def likes(lst: list, lang='eng') -> str:
    if len(lst) == 0:
        if lang != 'eng':
            return 'Никому не нравится '
        return 'No one likes this'
    if len(lst) == 1:
        if lang != 'eng':
            return f'{"".join(lst)} нравится это'
        return f'{"".join(lst)} likes this'
    if len(lst) == 2:
        if lang != 'eng':
            return f'{"".join(lst[0])} и {"".join(lst[1])} нравится это'
        return f'{"".join(lst[0])} and {"".join(lst[1])} like this'
    if len(lst) == 3:
        if lang != 'eng':
            return f'{"".join(lst[0])}, {"".join(lst[1])} и {"".join(lst[2])} нравится это'
        return f'{"".join(lst[0])}, {"".join(lst[1])} and {"".join(lst[2])} like this'
    else:
        if lang != 'eng':
            return f'{"".join(lst[0])}, {"".join(lst[1])} и {len(lst) - 2} остальным нравится это'
        return f'{"".join(lst[0])}, {"".join(lst[1])} and {len(lst) -2} others like this'


print(likes([]))
print(likes([], lang='rus'))
print(likes(['Ann']))
print(likes(['Ann'], lang='rus'))
print(likes(['Ann', 'Alex']))
print(likes(['Ann', 'Alex'], lang='rus'))
print(likes(['Ann', 'Alex', 'Mark']))
print(likes(['Ann', 'Alex', 'Mark'], lang='rus'))
print(likes(['Ann', 'Alex', 'Mark', 'Max']))
print(likes(['Ann', 'Alex', 'Mark', 'Max'], lang='rus'))
