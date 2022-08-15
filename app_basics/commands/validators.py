from typing import Tuple

from commands.constants import constants, EXIT_CMD


# raw_cmd = '//quit' # input from user
# // EXIT_CMD indexing
def is_command_valid(raw_cmd: str) -> Tuple[str, bool]:
    for slug, cmd in constants.items():
        if type(cmd) is not tuple:
            #error
            pass

        validation_result = raw_cmd in cmd
        if validation_result:
            return slug, True


def is_cmd(raw_cmd: str, cmd: str) -> bool:
    return is_command_valid(raw_cmd) and raw_cmd == cmd


def is_exit_cmd(raw_cmd: str):
    return is_cmd(raw_cmd, EXIT_CMD)


usr_input = 'assas//quit'
cmd_slug, is_valid_as_cmd = is_command_valid(usr_input)
print()

is_exit_cmd(usr_input)
