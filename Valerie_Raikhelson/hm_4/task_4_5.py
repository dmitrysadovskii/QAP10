a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

for k, v in a.items():
    for kk, vv in b.items():
        if k == kk:
            print(k)
            a[k] = [a[k], b[kk]]
            b[kk] = a[k]
        if k != kk:
            a[k] = [a[k], 'none']
        break

for k, v in b.items():
    if k != 'c':
        print(k, v)
        b[k] = ['none', b[k]]

print(a | b)
