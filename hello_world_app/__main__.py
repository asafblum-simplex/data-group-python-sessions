# TODO:
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/library/__main__.html#main-py-in-python-packages

# TODO: read - useful builtin modules
# https://docs.python.org/3/library/argparse.html#module-argparse
# https://docs.python.org/3/library/calendar.html#module-calendar
# https://docs.python.org/3/library/datetime.html#module-datetime
# https://docs.python.org/3/library/math.html#module-math
# https://docs.python.org/3/library/mimetypes.html#module-mimetypes
# https://docs.python.org/3/library/os.html#module-os
# https://docs.python.org/3/library/random.html#module-random
# https://docs.python.org/3/library/timeit.html#module-timeit


"""
__main__.py (not to be confused with __init__.py) acts as an entry point to our app when running from the cli.
It tells python what to execute when we execute the package(i.e. folder) directly.
"""
import sys

print(f"(*) running from {__file__}, \nmodule __name__ is {__name__}")

from app import cli_runner
cli_runner()

"""
Raise a SystemExit exception, signaling an intention to exit the interpreter.
The optional argument arg can be an integer giving the exit status (defaulting to zero), or another type of object. 

If it is an integer, 
    zero is considered “successful termination” 
    and any nonzero value is considered “abnormal termination” by shells and the like. 

    Most systems require it to be in the range 0–127, and produce undefined results otherwise. 
    Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally 
    underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors. 

If another type of object is passed[anything but an integer], 
    None is equivalent to passing zero, 
    and any other object is printed to stderr and results in an exit code of 1. 
        In particular, sys.exit("some error message") is a quick way to exit a program when an error occurs.

[Important - Remember this for later] 
Since exit() ultimately “only” raises an exception, it will only exit the process when called from the main thread, 
and the exception is not intercepted. 
Cleanup actions specified by finally clauses of try statements are honored, and it is possible to intercept the exit 
attempt at an outer level.

...

"""

sys.exit("Goodbye when an error occurs")
