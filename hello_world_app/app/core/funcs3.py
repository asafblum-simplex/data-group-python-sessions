from datetime import datetime

start_time = datetime.now()


def _reset_start_time():
    global start_time
    start_time = datetime.now()


def input_processor_factory(initial_counter=0):
    counter = initial_counter
    start_time = str(datetime.now())
    if counter is None:
        print("debug: assigned default numeric value to NaN value")
        counter = 0

    counter = initial_counter if initial_counter is not None else 0

    def increment_counter():
        global start_time
        nonlocal counter
        counter = 0



        start_time = "foo bar"
        if counter > 100:
            print(counter, start_time)

        counter += 1

    increment_counter()
    print(counter, start_time)
    return increment_counter  #


incrementer = input_processor_factory()

final_counter = inc_c()
print(final_counter)  # 2
final_counter[0] += 1  # 3
final_counter = inc_c()
print(final_counter)  # ? 5 | 4


def dispatch_cmd(cmd: str, *args, on_success, on_failure, **metadata):
    # prepare request body
    # send the request
    # wait for response
    # on response -> invoke callback

    response = {
        'status': 200,
        'body': {},
        'metadata': {}
    }

    if 200 <= response['status'] <= 299:
        return on_success('foo', 'bar', body=response['body'], status=response['status'])

    return on_failure(response['status'], response['body'])


def my_callback(value_one, *args, **kw):
    pass  # noop


my_args = ['foo', 'bar']
meta_data = {'tag': 'cron_job', 'current': '', 'env': 'dev'}
dispatch_cmd('users:grant:permission-admin', 'asd', on_success=my_callback, on_failure=my_callback, **meta_data)

my_func = input_processor_factory
my_value = 5
my_other_value = 5
my_value is my_other_value  # True

my_func is input_processor_factory  # True

my_func = input_processor_factory()

a = [1, 2, 3]
d = [1, 2, 3]
a is d  # False
b = a
c = a[:]

results = (a is b, b is c)

# usage of global global variable
c = 0


def add():
    global c  # try to uncomment this line and see what happens
    c = c + 2  # increment by 2
    print("Inside add():", c)


add()
