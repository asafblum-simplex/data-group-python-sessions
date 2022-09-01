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


# validators
def is_csv_line(payload: str) -> bool:
    raise NotImplementedError()


def is_local_path(payload: str) -> bool:
    raise NotImplementedError()


# handlers
def tail(payload: str) -> bool:
    raise NotImplementedError()


def head(payload: str) -> bool:
    raise NotImplementedError()


def quit_repl(payload: str) -> bool:
    raise NotImplementedError()


# commands

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
    start_time = NotImplemented

    while (raw_cmd := input(f'>>>')[2:]) != Command.QUIT:
        cmd, raw_path = raw_cmd.split(' ', 1)

        handler = commands.get(cmd)
        if not handler:
            print(f'Unknown command {cmd}, type help to list available commands')
            continue  # let the user try again

        print(f'Handling {cmd}... implement some logic')
        sleep(1)

    finished_time = NotImplemented
    elapsed = NotImplemented  # todo


if __name__ == '__main__':
    repl()
