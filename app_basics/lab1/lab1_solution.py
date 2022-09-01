import logging
from enum import Enum
from time import sleep

# logger
logger = logging.getLogger("automation_repl")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# module validators
def is_csv_line(payload: str) -> bool:
    raise NotImplementedError()


def is_local_path(payload: str) -> bool:
    raise NotImplementedError()


# module handlers
def tail(payload: str) -> bool:
    raise NotImplementedError()


def head(payload: str) -> bool:
    raise NotImplementedError()


def quit_repl(payload: str) -> bool:
    raise NotImplementedError()

COMMAND_PREFIX = '//'

commands = {
    'tail': tail,
    'head': head,
    'quit': quit_repl,
    'default': lambda x: x,
    'help': lambda x: x,
}


class Command(Enum):
    TAIL = 'tail'
    HEAD = 'head'
    QUIT = 'quit'
    DEFAULT = 'default'


def repl():
    while (raw_cmd := input(f'>>>')[2:]) != Command.QUIT:
        cmd, raw_path = raw_cmd.split(' ', 1)

        handler = commands.get(cmd)
        if not handler:
            print(f'Unknown command {cmd}, type help to list available commands')
            continue  # let the user try again
        print(f'Handling {}')
        sleep(1)


repl()
