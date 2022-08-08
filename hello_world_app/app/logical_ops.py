def one():
    print("one")
    return True


def two():
    print("two")
    return False


def three():
    print("three")
    return True




# __and__(True, False)
outcome = one() and two() and three()
outcome = two() and one() and three()
print()
#