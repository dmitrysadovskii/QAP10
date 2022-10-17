dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"c": 3, "d": 4, "e": 5}
dict_3 = {**dict_1, **dict_2}
for k, v in dict_3.items():
    dict_3[k] = [dict_1.get(k), dict_2.get(k)]
print(dict_3)
