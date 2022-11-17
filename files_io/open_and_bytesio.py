import io
import time

# see https://stackoverflow.com/questions/42800250/difference-between-open-and-io-bytesio-in-binary-streams
# see https://docs.python.org/3/library/functions.html#open
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