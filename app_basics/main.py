"""
Create a cli tool that will keep running, waiting for user input, evaluating and printing.

As a user, I want to be able to input a file path(hint, see os.path), apply head/tail on the file content, and see the output  (for example first 3 lines)
As a user, I want to be able to input a csv line,  apply head/tail on the line content, and see the output(for example first 3 columns)
As a user, I want to be able to be able to exit with a special command (for example '//exit')
As a user, I want to be able to input anything else and see only the head/tail
As a user, I want the program to output the accumulated first word of every line

The tool should print(meaningfully) the exact date and time in which it started, and in which it ended.

P.S Think what happens in the future, when product wants us to add a new command
"""
























import os

from loops import while_loop
import sys

from std_input_processing import line_processor, head, tail

if __name__ == '__main__':
    # active_handler_name = os.environ['PY_BASICS_LINE_PROCESSOR_OPERATION']
    # active_handler = locals()[active_handler_name]

    # if callable(active_handler):
    #     pass

    # todo: see https://docs.python.org/3/library/sys.html#sys.stdin
    for line in sys.stdin:
        # line_processor(line, active_handler)
        print(line)
        # sys.stdout.write(line)
        sys.stdout.flush()
