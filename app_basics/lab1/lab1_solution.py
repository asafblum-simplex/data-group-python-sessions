import logging
from enum import Enum
from time import sleep
from datetime import datetime

# logger
from typing import Callable, Dict

logger = logging.getLogger("automation_repl")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# region module .._constants
PROMPT = '>>> '
COMMAND_PREFIX = '//'
COMMAND_DELIM = ' '


# endregion

# region validators
def is_csv_line(line: str) -> bool:
    raise NotImplementedError()


def is_local_path(path: str) -> bool:
    raise NotImplementedError()


# endregion

def generic_cmd(*args, **kw):
    # generic_cmd_validator
    #
    return output

# region handlers
def tail(content: str, num_lines=5) -> bool:
    raise NotImplementedError()


def wordcount(content: str, num_lines=5) -> bool:
    raise NotImplementedError()

def head(content: str, num_lines=5) -> bool:
    raise NotImplementedError()


def quit_repl(msg: str, *extra) -> bool:
    raise NotImplementedError()


# endregion

# region commands

class Command(Enum):
    TAIL = 'tail'
    HEAD = 'head'
    QUIT = ('quit', 'exit', 'ex', 'e', 'q')
    EXIT = 'exit'
    HELP = 'help'
    # WORDCOUNT='wc'
    DEFAULT = 'default'


commands: Dict[str, Callable] = {

    # Command.WORDCOUNT.value: wordcount,
    Command.TAIL.value: tail,
    Command.HEAD.value: head,
    Command.QUIT.value: quit_repl,
    Command.EXIT.value: quit_repl,
    Command.DEFAULT.value: lambda x: x,
    Command.HELP.value: lambda x: x,
}
commands[Command.TAIL.value]()

EXIT_COMMANDS = (f'{COMMAND_PREFIX}{Command.QUIT.value}', f'{COMMAND_PREFIX}{Command.EXIT.value}')


# endregion


def repl():
    start_time = datetime.now()
    '//quit'

    while (raw_cmd := input(PROMPT)) not in EXIT_COMMANDS:
        if not raw_cmd.startswith(COMMAND_PREFIX):
            print(f'Invalid cmd {raw_cmd}, please try again')
            continue


        raw_cmd = raw_cmd[len(COMMAND_PREFIX):]
        commands[raw_cmd]

        cmd_parts = raw_cmd.split(' ')

        def our_print(msg: str):
            print(msg)

        cmds = {
            'PRINT': our_print
        }

        def default_handler(*args, **kw):
            pass

        handler = commands.get(cmd_parts[0], default_handler)

        print(f'Handling {cmd_parts[0]}... implement some logic')
        # ... handling ....

    finished_time = datetime.now()
    elapsed = finished_time - start_time


if __name__ == '__main__':
    repl()
