def input_processor_factory(initial_counter=0):
    counter = initial_counter

    if counter is None:
        print("debug: assigned default numeric value to NaN value")
        counter = 0

    counter = initial_counter if initial_counter is not None else 0
    counter = [counter]

    def inc_counter_by_2():
        def nested():
            nonlocal counter
            counter[0] += 1
            print(counter)

        nonlocal counter

        if counter[0] >= 100:
            counter[0] = 0

        nested()
        counter[0] += 1
        return counter

    return inc_counter_by_2


a = [1, 2, 3]
b = a
c = a[:]

results = (a is b, b is c)

inc_c = input_processor_factory()

final_counter = inc_c()
print(final_counter)  # 2
final_counter[0] += 1  # 3
final_counter = inc_c()
print(final_counter)  # ? 5 | 4

# usage of global global variable
c = 0


def add():
    global c # try to uncomment this line and see what happens
    c = c + 2  # increment by 2
    print("Inside add():", c)


add()
