s1, s2 = 'Robin Singh', 'I love arrays they are my favorite'
print(f'{s1.split(" ")}\n{s2.split(" ")}')

lst, s1, s2 = ['Ivan', 'Ivanou'], 'Minsk', 'Belarus'
print(f'Привет, {" ".join(lst)}! Добро пожаловать в {s1} {s2}')

lst = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(lst))

lst = list(i for i in range(0, 10))
lst.insert(3, -999)
lst.pop(6)
print(lst)

a, b, ab = {'a': 1, 'b': 2, 'c': 3}, {'c': 3, 'd': 4, 'e': 5}, {}

for k, v in {**a, **b}.items():
    if k in a and k in b:
        ab.update({k: [a[k], b[k]]})
    else:
        ab.update({k: [v, None]})
print(ab)
