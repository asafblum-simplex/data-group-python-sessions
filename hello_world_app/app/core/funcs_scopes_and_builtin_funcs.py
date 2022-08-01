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


root_lvl_var = "somne outside value"

from datetime import datetime


def scoping():
    lvl_one_var = "foo1"
    counter = 0

    def incre_counter():
        nonlocal counter

        counter += 1

    def my_nested_func():
        incre_counter()
        lvl_two_var = "foo2"

        print(root_lvl_var, lvl_one_var, lvl_two_var, f'counter: {counter}')

    return {
        # "inc": incre_counter,
        "my_nested_func": my_nested_func,

        "date": datetime.now()
    }


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
