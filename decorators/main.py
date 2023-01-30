from functools import wraps


def change_function(func):
    @wraps(func)
    def wrapper2(func_we_dont_need):
        @wraps(func_we_dont_need)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return wrapper2


def fizz():
    return "fuzz"

@change_function(fizz)
def foo():
    return "bar"


a = foo()
print()
def transactional(func):
    # @wraps(func)
    def with_transaction():
        print("trx is open")
        try:
            print(f"trx is opened for {func.__name__}")
            result = func()
            print(f"finished with {func.__name__}, result was")
            return result
        finally:
            print(f"trx is done for {func.__name__}")

    return with_transaction


@transactional
def my_logic():
    print("here is my logic inside a trx")


@transactional
def my_logic2():
    print("here is my logic2 inside a trx")


my_logic()
print("my_logic name: ", my_logic.__name__)
my_logic2()
