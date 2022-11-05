from collections import Counter

lst = [1, 5, 2, 9, 2, 9, 1]
print(''.join([str(k) for k, v in Counter(lst).items() if v == 1]))

test = 'shdf lsdfJKGTUYKKhFK"LKHaaaaaaksdnbnsafs?>>?<?></)(**^&%^!632328732  s'
d, lst = Counter(list(test.replace(' ', '').lower())), []
for k, v in d.items():
    if v == max(d.values()) and k.isalpha():
        lst.append(k)

print(sorted(lst)[0])
