"""
Create a cli tool that will keep running, waiting for user input, evaluating and printing.

$ python repl.py
repl >> {command} {...command_args} {filename}
...
repl >> {command} foo=bar fizz=fuzz fizz=fuzz fizz="fuzz fozz" {filename}
repl >> tail foo=bar fizz=fuzz fizz=fuzz fizz="fuzz fozz" ./foo.txt
"(.*)"
repl >> {command} foo=bar {filename}

raw_command.split(" ")

repl >> tail ./foo.txt
repl >> head ./foo.txt
repl >> head ./foo.txt
repl >> head <default number of lines = 3> ./foo.txt
repl >> head 10 ./foo.txt

As a user, I want to be able to input a file path(hint, see os.path), apply head/tail on the file content, and display the output  (for example first 3 lines)
As a user, I want to be able to input a csv line,  apply head/tail on the line content, and see the output(for example first 3 columns)
As a user, I want to be able to be able to exit with a special command (for example '//exit')
As a user, I want to be able to input anything else and see only the head/tail
As a user, I want the program to output the accumulated first word of every line

The tool should print(meaningfully) the exact date and time in which it started, and in which it ended.

P.S Think what happens in the future, when product wants us to add a new command
"""