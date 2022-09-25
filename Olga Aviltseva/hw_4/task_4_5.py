a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

a_copy = a.copy()
a_copy.update(b)

resultDict = {}

for key in a_copy.keys():
    resultDict[key] = [a.get(key), b.get(key)]

print(resultDict)
