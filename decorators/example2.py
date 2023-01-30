from typing import Callable


def conditional(function_with_condition: Callable[[], bool]):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            if function_with_condition():
                return func(*args, **kwargs)
            return None
        return wrapper
    return wrapper2


def is_dev_env() -> bool:
    return True


@conditional(is_dev_env)
def foo():
    return "zxasdwet"
@conditional(is_dev_env)
def foo():
    return "zxasdwet"

@conditional(is_dev_env)
def foo():
    return "zxasdwet"

@conditional(is_dev_env)
def foo():
    return "zxasdwet"