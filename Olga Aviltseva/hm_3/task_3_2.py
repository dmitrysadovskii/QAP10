text = "text no text"

text_divided = text.split()
result = ""
for i in text_divided:
    result += i + "ing "

print(result[0:-2])
