dict_1 = { 'a': 1, 'b': 2, 'c': 3}
dict_2 = { 'c': 3, 'd': 4,'e': 5}


def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
       else:
           dict_3[key] = [value, None]
   return dict_3

dict_3 = mergeDictionary(dict_1, dict_2)
print(dict_3)
