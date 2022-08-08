from nonlocal_vs_global import my_foo


def writing_func(foo):
    foo = 'fizz'

    local_foo = foo


    def nested():
        nonlocal local_foo
        local_foo = foo

        local_foo = "some new value"
        print(local_foo)

    nested()
    print()


writing_func('test_value')
print()
