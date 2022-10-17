arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(arr1[1])
arr2[3] = 9
print(arr2)
arr3 = arr1 + arr2
print(arr3)
arr4 = arr3[1:6]
print(arr4)
arr5 = arr4 + [10,11]
print(arr5)
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(a.intersection(b))
a = 2
b = 3
print(b and a)
print(a and b)
print(False and True)
print(False and False)
