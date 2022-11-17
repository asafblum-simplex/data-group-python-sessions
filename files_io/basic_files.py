from os import path
import pathlib


# my_current_path = pathlib.Path('./foo3.txt')
# fh = open(my_current_path, mode='rb')
# all_lines = fh.readlines()





def split_file_bytes_into_string(path_like, sep='\n'):
    container = {}

    while (current_byte := fh.read(1)) and current_byte == sep:
        if current_byte == sep:
            # case where current is the same as delim/sep
            pass
        else:
            # case where not
            pass

    first_byte = fh.read(1)

    fh.close()
    print()
