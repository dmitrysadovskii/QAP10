import random

hidden_num = input("number: ")

digits = set()
for _ in range(10):
    digits.add(random.randint(1, 9))
    if len(digits) == 4:
        break

number = int("".join(map(str, list(digits))))

list_of_hid_num = list(map(int, str(hidden_num)))
list_of_ran_num = list(digits)
print(number)
for i in list_of_hid_num:
    for l in list_of_ran_num:
        if i == l:
            if list_of_hid_num.index(i) == list_of_ran_num.index(l):
                print(i, "бык")
            else:
                print(i, "корова")
