import zipfile
import os
from pathlib import Path
#for python 3.5
directory = os.fsencode(os.curdir)
pathlist = Path(os.curdir)

for path in pathlist.glob('**/*.zip'):
        archive = zipfile.ZipFile(str(path))
        er = archive.testzip()
        if(archive.testzip() != None):
            print(path, er)
