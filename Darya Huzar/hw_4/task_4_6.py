nums = [1, 5, 2, 9, 2, 9, 1]
unique = []
for i in nums:
    if nums.count(i) == 1:
        unique.append(i)
print(*unique)
