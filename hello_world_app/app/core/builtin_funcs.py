# https://docs.python.org/3/library/functions.html#help
# https://docs.python.org/3/library/functions.html#hex
# https://docs.python.org/3/library/functions.html#pow
# https://docs.python.org/3/library/functions.html#round
# https://docs.python.org/3/library/functions.html#input

"""
# Scopes:
    # https://docs.python.org/3/library/functions.html#dir
    # https://docs.python.org/3/library/functions.html#globals
    # https://docs.python.org/3/library/functions.html#locals
"""

def testing_scope_visibility(foo, bar):
    _d, _l, _g = dir(), locals(), globals()
    print("Inside the function", _l, _g)


d, l, g = dir(), locals(), globals()
print("Outside the function", l, g)
testing_scope_visibility('fizz', 'fuzz')


