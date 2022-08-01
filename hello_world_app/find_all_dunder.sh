#!/usr/bin/env bash
PYTHON_LIB_DIR="$(pyenv root)/versions/$(pyenv global)/lib"
egrep -oh '__[A-Za-z_][A-Za-z_0-9]*__' "$PYTHON_LIB_DIR/*.py" | sort | uniq