import langid

str_names = input("Введите имена в формате: Анна, Евгений, Федор, Глафира \n").split(", ")
if len(str_names) == 0:
    print("no one likes this")
elif len(str_names) == 1:
    if langid.classify(str_names[0])[0] == "en":
        print(f"{str_names[0]} likes this")
    elif langid.classify(str_names[0])[0] == "ru":
        print(f"{str_names[0]} оценил(а) запись")
elif len(str_names) == 2:
    if langid.classify(str_names[0])[0] == "en":
        print(f"{str_names[0]} and {str_names[1]} likes this")
    elif langid.classify(str_names[0])[0] == "ru":
        print(f"{str_names[0]} и {str_names[1]} оценили запись")
elif len(str_names) == 3:
    if langid.classify(str_names[0])[0] == "en":
        print(f"{str_names[0]}, {str_names[1]} and {str_names[2]} likes this")
    elif langid.classify(str_names[0])[0] == "ru":
        print(f"{str_names[0]}, {str_names[1]} и {str_names[2]} оценили запись")
else:
    if langid.classify(str_names[0])[0] == "en":
        print(f"{str_names[0]}, {str_names[1]} and {len(str_names)-2} others like this")
    elif langid.classify(str_names[0])[0] == "ru":
        print(f"{str_names[0]}, {str_names[1]} и еще {len(str_names)-2} оценили запись")
