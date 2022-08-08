# https://docs.python.org/3/library/functions.html#help
# https://docs.python.org/3/library/functions.html#hex
# https://docs.python.org/3/library/functions.html#pow
# https://docs.python.org/3/library/functions.html#round
# https://docs.python.org/3/library/functions.html#input

"""
# Scopes:
    https://docs.python.org/3/reference/executionmodel.html#resolution-of-names

    scope-related builtin functions
    # https://docs.python.org/3/library/functions.html#dir
    # https://docs.python.org/3/library/functions.html#globals
    # https://docs.python.org/3/library/functions.html#locals
"""

# global scope

import math


def x(a, b, /, c):
    print(a, b, c)


x('this is a', b='this is b', c='this is c')


def a():
    def a2():
        def a3():
            print("aaaa")
            return 111

    print()
    return a2()

    return a2


my_test = a()


def input_processor_factory(initial_counter=0):
    counter = initial_counter

    if counter is None:
        print("debug: assigned default numeric value to NaN value")
        counter = 0

    counter = initial_counter if initial_counter is not None else 0

    def inc_counter_by_2():
        def nested():
            nonlocal counter
            counter += 1
            print(counter)

        nonlocal counter
        nested()
        counter += 1



    inc_counter_by_2()
    print(counter)


    def empty_input_handler():
        print("You must provide some input with valid data")
        return 'handled_computed_value'

    def extract_text(input_data):
        if not input_data:
            return empty_input_handler(), counter

        inc_counter()
        return f'---{input_data}', execution_counter

    inc_counter()
    print('other_arg', other_arg)
    return extract_text, execution_counter


input_processor_factory(None)
pending_files = ['/tmp/foo.txt', './a.txt', 'bbb', 'zzz', 'bbb', 'aaa']
pending_files.index('bbb')
print(pending_files)

pending_files = []  # clears the list
pending_files.sort()

input_processor = input_processor_factory('ll', '+x', '-h', src_dir='/usr/bin')  # chmod +x {file} && ll {flag}

print(f'Intermediate output: {extract_text_, execution_counter_}')

print()

#####
b = my_output()
print(b)  #
# "somne outside value"


decorator1 = scoping()
decorator2 = scoping()

decorator1()
decorator2()

print()


def testing_scope_visibility(foo, bar):
    # local/function scope

    fizz = "bar"
    print(my_outside_var)
    _d, _l, _g = dir(), locals(), globals()
    print("Inside the function", _d, _l, _g)


print(fizz)

d, l, g = dir(), locals(), globals()
print("Outside the function", d, l, g)
testing_scope_visibility('fizz', 'fuzz')


def sum(a, b):
    c = a + b

    if a < 0:
        return a, b, c

    if a > 5:
        return a * b

    if a > 50:
        return a / b

    if a > 500:
        return a ** b

    return a + b


calc = sum(-4, 5)
print()
if x()()():
    print("got in")
else:
    print("Not in")
print()
