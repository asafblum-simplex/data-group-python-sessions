class Foo:
    __my_member: str

    def __init__(self):
        self.__my_member = "some value"

    @property
    def my_member(self):
        return self.__my_member

    def my_func(self):
        pass


my_foo = Foo()
a = my_foo.my_member

my_foo.my_member
my_foo.my_logic()
