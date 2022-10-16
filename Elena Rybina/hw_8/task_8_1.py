def typed(type):
    def decorator(wrap_to_decorate):
        def wrapper(*args):
            if type=='str':
                wrap_to_decorate(''.join(map(str,args)))
            if type=='int':
                wrap_to_decorate(sum(map(int,args)))
            if type=='float':
                wrap_to_decorate(sum(map(float,args)))

        return wrapper
    return decorator
    @typed












