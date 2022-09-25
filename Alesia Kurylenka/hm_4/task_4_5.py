dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'c': 3, 'd': 4, 'e': 5}

dict_1_copy = dict_1.copy()
dict_1_copy.update(dict_2)
dict_3 = {}
for k in dict_1_copy.keys():
    dict_3[k] = [dict_1.get(k), dict_2.get(k)]

print(dict_3)
