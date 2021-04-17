from zipfile import ZipFile
from files_dir_lists import get_dir
import os.path

def in_archive(zip_name, file_ext):
    fl_list = get_dir(".", file_ext, False)
    for el in fl_list[0]:
        with ZipFile(zip_name, 'a') as archive:
            archive.write(el)
    return os.path.isfile(zip_name):

print(in_archive("zip_archive", ".txt"))