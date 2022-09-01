from uuid import uuid4

comp_dict = {f'{uuid4()}-{x}': i for i in range(10, 15) for x in range(3)}
nested_comp_dict = {f'{uuid4()}:{x}': i ** 2 for i in range(20, 25) for x in range(3) for y in range(15, 20)}

# will not work! why?
# nested_comp_dict = {f'{uuid4()}:{x}': i ** 2 for i in range(y, y + 10) for x in range(3) for y in range(100, 103)}

# created a dict with a value of a generated list for each iteration
dict_comp_list = {f'{uuid4()}:{x}': [i ** 2 for i in range(y, y + 10) for u in range(x, x + 10)] for x in range(3) for y
                  in range(100, 103)}

with open("/Users/asafblum/workspace/learning/apt-team-python-sessions/big_file.txt") as fh:
    # working
    fh.closed
    pass


async def foo():
    pass
