import os
import time
import shutil

path = "C:\\Users\\micro\\OneDrive\\Desktop\\Projects\\WhtjrProjs\\Projs\\(3)PRO-C99 BACKUP FILES\\Trash"
print(path)
time = time.time()


def ctimeFunction():
    ctime = os.stat(path).st_ctime
    return ctime


if os.path.exists(path):
    for root_folders, folder, files in os.walk(path):
        ctime = ctimeFunction()
        if ctime < time:
            if os.path.isdir(root_folders):
                shutil.rmtree(path)
            elif os.path.isfile(files):
                os.remove(files)
else:
    print("File/Folder not found")
