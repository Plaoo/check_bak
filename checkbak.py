import zipfile
import os
import rarfile
import lzma
import multiprocessing

from pathlib import Path

# for python 3.5
directory = os.fsencode(os.curdir)
pathlist = Path(os.curdir)


# controllo gli zip in modo ricursivo
def checkzip(path):
    for path in pathlist.glob('**/*.zip'):
        archive = zipfile.ZipFile(str(path))
        print(archive)
        er = archive.testzip()
        if (archive.testzip() != None):
            print(path, er)


# controllo i rar in modo ricursivo
def check7z(path):
    for path in pathlist.glob('**/*.7z'):
        archive = lzma.open(str(path), "r")


    pass


if __name__ == "__main__":

    checkzip(pathlist)
