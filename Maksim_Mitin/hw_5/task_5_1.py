import langid

string = input("Enter user names (Введите имена пользователей  ) \n").split(", ")


def likes(some_string):
    if len(some_string) == 0:
        print("No one likes this ")
    elif langid.classify(some_string[0])[0] == "en":
        if len(some_string) == 1:
            print(f"{str(some_string[0])} likes this")
        elif len(some_string) == 2:
            print(f"{str(some_string[0])} and {str(some_string[1])} likes this")
        elif len(some_string) == 3:
            print(f"{str(some_string[0])},{str(some_string[1])} and {str(some_string[2])} likes this")
        else:
            print(f"{str(some_string[0])},{str(some_string[1])} and {len(some_string[2:])} others like this")
    elif langid.classify(some_string[0])[0] == "ru":
        if len(some_string) == 1:
            print(f"{str(some_string[0])} оценил(а) это")
        elif len(some_string) == 2:
            print(f"{str(some_string[0])} и {str(some_string[1])} оценили это")
        elif len(some_string) == 3:
            print(f"{str(some_string[0])},{str(some_string[1])} и {str(some_string[2])} оценили это")
        else:
            print(f"{str(some_string[0])},{str(some_string[1])} и {len(some_string[2:])} оценили это")
    else:
        print("Unauthorized Language - Невозможно определить язык")


likes(string)
