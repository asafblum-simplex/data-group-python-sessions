import filecmp
import os
import fileinput
import shutil
import pathlib
a = pathlib.Path('/tmp')
shutil.copystat('input/a.txt', 'input/b.txt')

input_result = input("foo?")
print(f'answer was {input_result}')

for i in range(1):
    print(f'**** {input("asdasd")}')


for line in fileinput.input(encoding="utf-8"):
    print(f'---{line}')



# urllib.open

cwd = os.path.dirname(os.path.realpath(__file__))

res_a_b = filecmp.cmp('./input/a.txt', './input/b.txt')
res_a_c = filecmp.cmp('./input/a.txt', './input/c.txt')

# compare the file list in 2 folders
diff_folders = filecmp.dircmp(f'input', f'output')
diffs = [
    diff_folders.common_files,
    diff_folders.diff_files,
    diff_folders.common,
    diff_folders.common
]

print()


