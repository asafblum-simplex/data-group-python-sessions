from functools import wraps
from datetime import datetime

my_var = "xxxx"

def deco_with_customization(param, param2):
    #
    def basic_deco(func_to_wrap):
        @wraps(func_to_wrap)
        def inner(*args, **kw):  # to preserve the behaviour

            #
            def
            # wrapping the function
            # before
            result = func_to_wrap(*args, **kw)  # excecution
            # end/finally/after
            return result

        return inner

    return basic_deco

@basic_deco
def hello_world(name, age):
    print(name, age)
    return f"{name} {age}"



hello_world()



def repeat(num_times):  # arguemnts to customize the behaviour of the decorator
    """
    runs the given function <code>num_times</code>
    """

    def decorator_repeat(func):  # only and always a single argument of type function (i.e. `callable(func) is True`)
        @wraps(func)
        # these are the actual arguemnts/params that the wrapped function expects to get
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)

            return value

        return wrapper_repeat

    return decorator_repeat


def timing(time_offset=1, max_timeout=2):
    print(time_offset, max_timeout)

    def wrapper(func):
        @wraps(func)
        def with_timing(*nested_args, **nested_kwargs):
            start = datetime.utcnow()
            try:
                result = func(*nested_args, **nested_kwargs)
            finally:
                end = datetime.utcnow()
                elapsed = end - start
                print(f'{func.__name__} took {elapsed}')

            return result

        return with_timing

    return wrapper

@deco(param)
def auditing(under_audtining_func):
    @wraps(under_audtining_func)
    def with_auditing(*nested_args, **nested_kwargs):
        try:
            result = under_audtining_func(*nested_args, **nested_kwargs)
            print("after func", result)
            print(my_var)
            return result
        except:
            print("during func error")
        finally:
            print("always after func, nevermind if error or not")

    return with_auditing


@timing(time_offset=10, max_timeout=120)
# @auditing
def sensitive_compute(amount: float, username: str) -> str:
    return f"comp sensitive data for {username} with amount of {amount}"


#
# @timing
# @auditing
# def store_to_s3(bucket: str, suffix: str) -> bool:
#     print('store_to_s3', bucket, suffix)
#     return True
#
#
# @timing
# @auditing
# def fetch_user_cards(user_id: int):
#     return f"fetch cards for {user_id} "


sensitive_compute(43, username='asaf')
# store_to_s3('my_data', 'foo.parquest')
# fetch_user_cards(400)

# sensitive_compute = auditing(sensitive_compute)
sensitive_compute()

# first class citizen


# ???
# my_auditiable_name = my_auditiable.__name__
# print()
