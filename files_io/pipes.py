#!/usr/bin/env python

# python pipes.py
# ./fancy_lines_tranformer

import fileinput
import sys

# method 1
print(sys.argv)
try:
    input_filename = sys.argv[1]
except IndexError:
    input_stream = sys.stdin

else:
    input_stream = open(input_filename, 'r')

try:
    for line in input_stream:
        print("processed", line)  # do something useful with each line
except KeyboardInterrupt:
    print("Goodbye!")

exit(0)

# method 2
with fileinput.input() as f_input:
    for line in f_input:
        print("processed:", line, end='')

# $ ls | ./pipes.py          # Prints a directory listing to stdout.
# $ ./filein.py /etc/passwd   # Reads /etc/passwd to stdout.
# $ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.
