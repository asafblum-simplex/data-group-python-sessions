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

from commands.validators import is_exit_cmd

my_struct = {
    'user_id': int,
    'username': str,
    'created_at': int
}

def my_request_handler(req, res):
    if FEATURE_FLAG:
        from commands.validators import is_exit_cmd

    pass


'/user/{id}/status', my_request_handler

if __name__ == '__main__':
    counter: int = 0

    while True:
        counter += 1

        current_line: str = '//exit'  # todo: populate

        if is_exit_cmd(current_line):
            break

        print(f'iteration number {counter}')

    # ... final seq, shutdown, clean up - stuff to do
