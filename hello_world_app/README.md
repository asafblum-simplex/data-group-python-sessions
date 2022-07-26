
## [Glossary (link)](https://docs.python.org/3/glossary.html)
module, regular package, package, namespaces package

## [CMD Line(Docs - link)](https://docs.python.org/3/using/cmdline.html)

### `python -c 'python code'`
Execute the Python code in `python code`.`python code` can be one or more statements separated by newlines, with significant leading whitespace as in normal module code. <br>
If this option is given:
* the first element of sys.argv will be "-c" and
* the current directory will be added to the start of sys.path(allowing modules in that directory to be imported as top level modules).

Raises an auditing event cpython.run_command with argument command.

### `python -m <module-name>`
Search `sys.path` for the named module `module-name` and execute its contents as the `__main__` module.

If this option is given, the first element of sys.argv will be the full path to the module file
(while the module file is being located, the first element will be set to `-m`).
As with the `-c` option, the current directory will be added to the start of sys.path.

Raises an auditing event cpython.run_module with argument module-name.

#### Notes regarding `module-name`:
* Since the argument is a module name, you must not give a file extension (.py).
* The module name should be a valid absolute Python module name,
  * but the implementation may not always enforce this (e.g. it may allow you to use a name that includes a hyphen).
* Package names (including namespace packages) are also permitted.
* When a package name is supplied instead of a normal module, the interpreter will execute `<pkg>.__main__` as the main
module.
  * This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the
  interpreter as the script argument.
  ...

`-I` option can be used to run the script in isolated mode where `sys.path` contains neither
    the current directory nor the user’s site-packages directory.<br>
    All `PYTHON*` environment variables are ignored, too.



#### Note: 
Many standard library modules contain code that is invoked on their execution as a script. An example is the timeit module:
    
    python -m timeit -s 'setup here' 'benchmarked code here'
    python -m timeit -h # for details

