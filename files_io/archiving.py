import tempfile
from pathlib import Path
from zipfile import ZipFile

import os

with open("./b.zip", 'wb') as temp_fh, ZipFile(temp_fh, 'w') as archive:
    # with os.scandir('./') as files:
        # for file in files:
        #     print(file)
    archive.write(Path('./'))
