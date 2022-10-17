lst = ["abc", "bac", "cad", "dac"]
for i in lst:
    for y in i:
        print (y,end="-")



ints = [1, 2, 3, 4]
a = len(ints)

for i in range(a):
    ints[i] = float(ints[i])
print(ints)
