string = 'run like Forest Gump'
list_of_words = string.split()
for i in list_of_words:
    string_plus_ing = i.join(('', 'ing'))  # можно и сразу на печать выводить просто сделал отдельную переменную
    print(string_plus_ing)
