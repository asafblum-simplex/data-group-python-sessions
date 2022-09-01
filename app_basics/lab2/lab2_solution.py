def fizz_buzz(current=1, stop=50):
    # todo solve the issue with a big stop
    # todo try to improve this function

    if current >= stop:
        return

    if current % 3 == 0:
        print("Fizz")

    elif current % 5 == 0:
        print("Fuzz")
    else:
        print(current)

    fizz_buzz(current + 1, stop)


def fibonacci(n, f1=0, f2=1, acc=0):
    # todo solve the issue with a big n
    # todo add descriptive doc string

    if n - 1 == 0:
        return f1, acc + f1
    else:
        return fibonacci(n - 1, f2, f1 + f2, acc + f1)

