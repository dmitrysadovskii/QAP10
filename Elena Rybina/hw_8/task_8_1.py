def typed(data_type):
    def inner(func):
        def wrapper(*args):
            if data_type == 'str':
                func(''.join(map(str, args)))
            if data_type == 'int':
                func(sum(map(int, args)))
            if data_type == 'float':
                func(sum(map(float, args)))
        return wrapper
    return inner


@typed(data_type='str')
def add_two_symbols(*args):
    print(args)


@typed(data_type='int')
def add_three_symbols(*args):
    print(args)


@typed(data_type='float')
def add_four_symbols(*args):
    print(args)

add_two_symbols("3", "a")
add_three_symbols(1, "2")
add_four_symbols(0.1, 0.2, 0.4, 0.7)
