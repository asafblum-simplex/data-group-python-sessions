"""
Create a cli tool that will keep running, waiting for user input, evaluating and printing.

As a user, I want to be able to input a file path(hint, see os.path), apply head/tail on the file content, and see the output  (for example first 3 lines)
As a user, I want to be able to input a csv line, apply head/tail on the line content, and see the output(for example first 3 columns)
As a user, I want to be able to be able to exit with a special command (for example '//exit')

As a user, I want to be able to input anything else and see only the head/tail
As a user, I want the program to output the accumulated first word of every line

The tool should print(meaningfully) the exact date and time in which it started, and in which it ended.


save current user input, while input is not exact match '//exit', keep running... (while loop with condition)

testing conditions for each line:

1. test if 'exit' cmd, if true -> somehow to exit the while loop -
"""
from constants.commands import EXIT_CMD, SEND_REQUEST_CMD



if __name__ == '__main__':
    counter: int = 0

    while True:
        counter += 1

        current_line: str = '//exit'  # todo: populate

        if is_exit_cmd(current_line):
            break

        print(f'iteration number {counter}')

    # ... final seq, shutdown, clean up - stuff to do
