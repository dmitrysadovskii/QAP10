a = {'a': 1, 'b': 2, 'c': 3}  # Есть 2 словаря
b = {'c': 3, 'd': 4, 'e': 5}


print('update:', a.update(b))
print('**:', {**a, **b})