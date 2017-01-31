from os import listdir, rename
from os.path import isfile, join
from os import chdir


def rename_files():
    mypath = "F:\\tmp\\pics"
    only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    trltTable = str.maketrans("", "", "0123456789")
    print(trltTable)
    chdir(mypath)
    for file in only_files:
        rename(file, file.translate(trltTable))


rename_files()
