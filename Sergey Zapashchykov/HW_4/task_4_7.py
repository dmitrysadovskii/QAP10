from collections import Counter

text = 'a' * 9000 + 'b' * 9000 + ',' * 500 + '   ' * 20 + '1' * 20 + 'n' * 9000
text_to_list = list()

for i in text.lower():
    if i.isalpha():
        text_to_list.append(i)

c = Counter(text_to_list)
print(c)
v = c.most_common(1)
print(v)
w = v[0][0]
print(f'Самая частая буква: {w}')
