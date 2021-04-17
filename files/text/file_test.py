import os.path

for root, dirs, files in os.walk("."):
    print(dirs)
    print(files)