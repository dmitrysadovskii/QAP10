likes = ['Анна', 'Алекс', 'Марк', 'Петя', 'Антон']

if len(likes) == 0:
    print('No one likes this')
elif len(likes[0]) == len(likes[0].encode()):
    if len(likes) == 1:
        print(likes[0], 'likes this')
    elif len(likes) == 2:
        print(f'{likes[0]} and {likes[1]} like this')
    elif len(likes) == 3:
        print(f'{likes[0]}, {likes[1]} and {likes[2]} like this')
    else:
        print(f'{likes[0]}, {likes[1]} and {len(likes) - 2} others like this')
else:
    if len(likes) == 1:
        print(likes[0], 'нравится это')
    elif len(likes) == 2:
        print(f'{likes[0]} и {likes[1]} нравится это')
    elif len(likes) == 3:
        print(f'{likes[0]}, {likes[1]} и {likes[2]} нравится это')
    else:
        print(f'{likes[0]}, {likes[1]} и {len(likes) - 2} другим нравится это')
