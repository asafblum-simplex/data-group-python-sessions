# todo: __all__ dunder variable
from app.common import *

from .common.user_vars import username, ip, email
from app.core.greeter import greet_user


def cli():
    # TODO:
    import __main__
    print(__main__.__spec__, 'xxxxx')

    print(f"CLI: __name__: {__name__}, __package__: {__package__} (logged in with {email})")
    greet_user(username, ip)

    # todo: use sys_info
