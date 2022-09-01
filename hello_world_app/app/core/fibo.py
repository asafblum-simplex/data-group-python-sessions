# Fn = Fn-1 + Fn-2
def fibonacci(n, f1, f2):
    if n - 1 == 0:
        return f1
    else:
        return fibonacci(n - 1, f2, f1 + f2)




if __name__ == "__main__":
    print(fibonacci(10, 0, 1))

