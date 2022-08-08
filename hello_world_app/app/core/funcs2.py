

def func1(arg1, arg2):
    """
    :param arg1 the index of the user
    :param arg2 the index of the machine
    Accept a special argument and converts it to binary...

    >>> print("x")
    """
    func2(arg1 + '1', arg2 + '1')


def func2(arg1, arg2):
    func3(arg1 + '2', arg2 + '2')


def func3(arg1, arg2):
    print("func3", arg1 + '3', arg2 + '3')


if __name__ == "__main__":
    func1("foo", "bar")



