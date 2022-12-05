import io
import time
from typing import List, Tuple

# file = "400,x,y,z,50,trueeeeeeeeeeeeeeeeee,null"
DELIMITER = ','

io.BlockingIOError


# not to do, not scalable! file size can be large, we will take up a lot of ram
def z():
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


def with_offsets():
    with open("foo.txt") as fh:
        offsets = compute_offsets(fh)
        len_of_field5_content = field_value_len(5, offsets)
        len_of_field1_content = field_value_len(1, offsets)


######


# 1

begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
seconds = end - begin
print("Concat:", seconds)

# 2
begin = time.time()
buffer_io = io.BytesIO()
with open("test.dat", "wb") as f:
    for i in range(0, 50000):
        buffer_io.write(b"Hello World")

        if len(buffer_io.getbuffer()) >= 1024:
            f.write(buffer_io.getvalue())
            buffer_io.flush()

end = time.time()
seconds = end - begin
print("BytesIO:", seconds)

with open("test.dat", "wb") as f:
    f.write(buffer)
    f.write(buffer_io.getvalue())

# further reading
# see https://stackoverflow.com/questions/42800250/difference-between-open-and-io-bytesio-in-binary-streams
# see https://docs.python.org/3/library/functions.html#open

# archiving further reading
# https://stackoverflow.com/a/20765054
