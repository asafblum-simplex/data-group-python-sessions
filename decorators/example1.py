from functools import wraps

# https://github.com/GrgoMariani/Python-Decorators


ENV = 'prod'


def change_function(func):
    @wraps(func)
    def wrapper2(func_we_dont_need):
        @wraps(func_we_dont_need)
        def wrapper(*args, **kwargs):
            if ENV == 'dev':
                return func_we_dont_need(*args, **kwargs)

            return func()

        return wrapper

    return wrapper2


def replacment():
    return "something else"


@change_function(replacment)
def foo():
    return "zxczxczxcc"


a = foo()
print()
