# https://docs.python.org/3/py-modindex.html
import sys


def sys_information():
    """
    sys.version - A string containing the version number of the Python interpreter plus additional information on the build
    number and compiler used. This string is displayed when the interactive interpreter is started. Do not extract version
    information out of it, rather, use version_info and the functions provided by the platform module.

    sys.executable - A string giving the absolute path of the executable binary for the Python interpreter, on systems
    where this makes sense.
    If Python is unable to retrieve the real path to its executable, sys.executable will be an empty string or None.

    sys.argv - The list of command line arguments passed to a Python script.
     - argv[0] is the script name (it is operating system dependent whether this is a full pathname or not).
     - If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'.
     - If no script name was passed to the Python interpreter, argv[0] is the empty string.

    sys.orig_argv - The list of the original command line arguments passed to the Python executable (New in version 3.10).
    """

    loaded_builtin_modules = sys.builtin_module_names

    return f"""
    Using python version {sys.version} {sys.executable}
    Implementation: {sys.implementation}
    CLI input arguments: {sys.argv}
    
    Total of {len(loaded_builtin_modules)} loaded builtin modules, preview:
    \t{loaded_builtin_modules[0:5]}
    """


def install_audit():
    """
    sys.audit(event, *args)
    Raise an auditing event and trigger any active auditing hooks. event is a string identifying the event, and args may contain optional arguments with more information about the event. The number and types of arguments for a given event are considered a public and stable API and should not be modified between releases.

    For example, one auditing event is named os.chdir. This event has one argument called path that will contain the requested new working directory.

    sys.audit() will call the existing auditing hooks, passing the event name and arguments, and will re-raise the first exception from any hook. In general, if an exception is raised, it should not be handled and the process should be terminated as quickly as possible. This allows hook implementations to decide how to respond to particular events: they can merely log the event or abort the operation by raising an exception.

    Hooks are added using the sys.addaudithook() or PySys_AddAuditHook() functions.

    The native equivalent of this function is PySys_Audit(). Using the native function is preferred when possible.

    See the audit events table for all events raised by CPython.

    New in version 3.8.
    """

    def audit_handler(event, args):
        if event == 'code.__new__':
            print(f'audit: {event} with args={args}')
        if event == 'os.mkdir':
            print(f'audit: {event} with args={args}')

    sys.addaudithook(audit_handler)


