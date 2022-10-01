from collections import Counter

original_text = "j hijb2i 1ihIIIIIIIIbbbbbbbbbbbbbbbbbbibIen2b3 $%^&*b wIebi**&^dIIIIIIIikbd efh  /.,mefwfIu whf w - dvib- i- dfv dabebhiiubeb vie"
text_mod = list()

for i in original_text.lower():
    if i.isalpha():
        text_mod.append(i)

c = Counter(text_mod)
max_number = max(list(c.values()))
list_max_numbers = []

for k, v in c.items():
    if v == max_number:
        list_max_numbers.append(k)

list_max_numbers.sort()
print(f"Result: {list_max_numbers[0]}")
