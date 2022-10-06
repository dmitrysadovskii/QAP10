def likes(*args):
    if len(args) == 0:
        print("No one likes this")
    elif len(args) == 1:
        print(f"{str(args[0])} likes this")
    elif len(args) == 2:
        print(f"{str(args[0])} and {str(args[1])} likes this")
    elif len(args) == 3:
        print(f"{str(args[0])},{str(args[1])} and {str(args[2])} likes this")
    else:
        print(f"{str(args[0])},{str(args[1])} and {len(args[2:])} others like this")


