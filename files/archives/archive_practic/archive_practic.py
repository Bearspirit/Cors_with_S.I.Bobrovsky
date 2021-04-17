import os.path
from zipfile import ZipFile


def in_archive(zip_name, file_ext):
    for roots, dirs, files in os.walk('.'):
        for el in files:
            if file_ext in el:
                with ZipFile(zip_name, 'a') as archive:
                    archive.write(el)
    if os.path.isfile(zip_name):
        return True
    else:
        return False

print(in_archive("zip_archive", ".txt"))