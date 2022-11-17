import io

import json


def x():
    content = """
            some data 1111 2222 3333 4444
            xcxcxcv
            asdasad
            qweqweqwe
            dfgdfg

            """

    with open('./config.ini', 'w+', encoding='utf8') as fh:
        fh.write(content)

        fh.seek(0)
        headerVersion = fh.read(4)
        curr_pos = fh.tell()
        mime = fh.read(3)

        fh.seek(25)
        ext = fh.read()

        fh.write("my_first_key=my_first_value")

        fh.write("my_2ed_key=my_2ed_value")

        val = fh.read()
        print("val", val)



    try:
        fh.write('asda')
    except:
        print("fh was closed")
    if headerVersion == 'asdasd':
        pass


data = {'devId': 12, 'status': 'online'}
with open("/tmp/my_data.json", "w") as fh:
    json.dump(data, fh)


with open("/tmp/my_data.json") as fh:
    loaded_data = json.load(fh)

a = {
    # """ddddd"""
    "asdasd": "zc"
}
print()