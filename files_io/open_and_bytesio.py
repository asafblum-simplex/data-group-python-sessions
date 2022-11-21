import io
import time
from typing import List, Tuple

# file = "400,x,y,z,50,trueeeeeeeeeeeeeeeeee,null"
DELIMITER = ','

# not to do, not scalable! file size can be large, we will take up a lot of ram
with open("some_big_file") as fh:
    content_lines: List[str] = fh.readlines()

    results = []
    for line in content:
        result = do_some_processing(line)
        results.append(result)

    fh.write('\n'.join(results))
    print()


def compute_offsets(fh) -> List[int]:
    offsets = []
    previous_offset = 0
    while True:
        previous_offset = fh.tell()
        char = fh.read(1)

        if previous_offset == fh.tell():
            # EOF
            return offsets

        if char == DELIMITER:
            offsets.append(fh.tell())


def field_value_len(field_number: int, offsets) -> int:
    return offsets[field_number] - offsets[field_number - 1]


with open("file") as fh:
    offsets = compute_offsets(fh)
    len_of_field5_content = field_value_len(5, offsets)
    len_of_field1_content = field_value_len(1, offsets)

######
begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
seconds = end - begin
print("Concat:", seconds)

begin = time.time()
buffer = io.BytesIO()
for i in range(0, 50000):
    buffer.write(b"Hello World")
end = time.time()
seconds = end - begin
print("BytesIO:", seconds)

buffer = io.BytesIO()
# ...
with open("test.dat", "wb") as f:
    f.write(buffer.getvalue())

# further reading
# see https://stackoverflow.com/questions/42800250/difference-between-open-and-io-bytesio-in-binary-streams
# see https://docs.python.org/3/library/functions.html#open

# archiving further reading
# https://stackoverflow.com/a/20765054
