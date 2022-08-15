from typing import Tuple

from commands.constants import constants


# todo not finished.
# todo: notice i have renamed it to resolve_cmd and changed the return value
def resolve_cmd(raw_cmd: str) -> str:
    """
    Usage example:
    is_command_valid(raw_cmd = '//quit')
    # ('EXIT_CMD', True)
    """

    for slug, cmd in constants.items():
        validation_result = raw_cmd in cmd
        if validation_result:
            return slug


def is_cmd(raw_cmd: str, cmd: Tuple) -> bool:
    return resolve_cmd(raw_cmd) is not None and raw_cmd in cmd


def is_exit_cmd(raw_cmd: str):
    return is_cmd(raw_cmd, constants['EXIT_CMD'])


usr_input = '//quit'
if is_exit_cmd(usr_input):
    print('Got EXIT command')
    exit(0)

