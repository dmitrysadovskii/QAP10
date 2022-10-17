from collections import Counter

text = "...Aaa   BbbB/////"
text = ''.join(ch for ch in text.lower() if ch.isalpha())
print(sorted(Counter(text).items(), key=lambda x: (-x[1], x[0]))[0][0])
