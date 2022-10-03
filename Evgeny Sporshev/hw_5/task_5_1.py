likes_list = ["Ann", "Alex", "Mark", "Max"]
russian_letters = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л',
                   'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']
if likes_list == []:
    print('no one likes this')
elif len(likes_list) == 1:
    if likes_list[0][0].lower() in russian_letters:
        print(likes_list[0], 'любит это')
    else:
        print(likes_list[0], 'likes this')
elif len(likes_list) == 2:
    if likes_list[0][0].lower() in russian_letters:
        print(f'{likes_list[0]} и {likes_list[1]} любят это')
    else:
        print(f'{likes_list[0]} and {likes_list[1]} like this')
elif len(likes_list) == 3:
    if likes_list[0][0].lower() in russian_letters:
        print(f'{likes_list[0]}, {likes_list[1]} и {likes_list[2]} любят это')
    else:
        print(f'{likes_list[0]}, {likes_list[1]} and {likes_list[2]} like this')
else:
    if likes_list[0][0].lower() in russian_letters:
        print(f'{likes_list[0]}, {likes_list[1]} и {len(likes_list) - 2} других любят это')
    else:
        print(f'{likes_list[0]}, {likes_list[1]} and {len(likes_list) - 2} others like this')
