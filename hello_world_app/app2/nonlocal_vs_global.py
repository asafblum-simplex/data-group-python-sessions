my_foo = "my_bar"
def x(foo):
    def nested():
        nonlocal foo
        print(foo)

    print('1', nested())
    foo = "fizz"
    print('2', foo)
    # global foo
    print(foo)
    foo = 'bar'

    return f'****{foo}'
