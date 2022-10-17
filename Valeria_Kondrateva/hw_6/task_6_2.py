import collections
string = input("Введите строку ")
count_dict = dict(collections.Counter(string))
strings = []
for key, value in count_dict.items():
    if value == 1:
        strings.append("{}{}".format(key, ""))
    else:
        strings.append("{}{}".format(key, value))
result = "".join(strings)

print(result)
