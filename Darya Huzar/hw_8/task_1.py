def typed(type):
    def decorator(func):
        def wrapper(*args):
            list = []
            if type == 'str':
                for i in args:
                    list.append(str(i))
                return func(*list)
            elif type == 'int':
                for i in args:
                    list.append(float(i))
                return func(*list)

        return wrapper
    return decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
