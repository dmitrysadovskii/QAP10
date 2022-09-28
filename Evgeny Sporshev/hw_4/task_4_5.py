a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

for k, v in {**a, **b}.items():
    if k in a and k in b:
        ab.update({k: [a[k], b[k]]})
    elif k in a and k not in b:
        ab.update({k: [v, None]})
    else:
        ab.update({k: [None, v]})

print(ab)
