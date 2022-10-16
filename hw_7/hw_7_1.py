def typed(type):
    def decorator(func):
        def wrapper(*args):
            if type == 'str':
                s = ''
                for i in args:
                    s += str(i)
                func(s)
            elif type == 'int':
                s = 0
                for i in args:
                    s += int(i)
                func(s)
            else:
                s = 0
                for i in args:
                    s += float(i)
                func(s)
            return s

        return wrapper

    return decorator


@typed(type='str')
def add_two_symbols(*args):
    print(args)


@typed(type='int')
def add_three_symbols(*args):
    print(args)


@typed(type='float')
def add_float_symbols(*args):
    print(args)


add_two_symbols("3", 5)
add_two_symbols(5, 5)
add_two_symbols('a', 'b')
add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_float_symbols(0.1, 0.2, 0.4)
