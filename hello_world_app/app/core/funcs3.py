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
