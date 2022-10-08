likes = ("Ann", "Alex", "Mark", "Max")
# likes = "Ann"
# likes = ("Ann", "Alex")
# likes = ("Ann", "Alex", "Mark")
a = len(likes)

print('Колличество лайков: ', a)

if likes == 0:
    print("no one likes this.")
elif type(likes) == str:
    print(f" {likes} like this.")
elif a == 2:
    print(" and ".join(likes), "like this.")
elif a == 3:
    print(likes[0], ',', likes[1], "and", likes[2], 'like this.')
elif a >= 4:
    print(likes[0], ',', likes[1], 'and 2 others like this.')
