my_rng = range(0, 100)
my_rng_iter = iter(my_rng)


my_enumeration = enumerate('abcdef', 100)
first_value = next(my_enumeration)


def return_tup():
    my_tuple = ('foo', 'bar')
    return my_tuple


foo = "bar"





for index, char in my_enumeration:

    if index > 4:
        print(char * 100)

output2 = []
for i in my_rng:
    output2.append(f'machine-{i * i}')



print()
