a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}

for k, v in {**a, **b}.items():
    if k in a and k in b:
        ab.update({k: [a[k], b[k]]})
    else:
        ab.update({k: [v, None]})
print(ab)
