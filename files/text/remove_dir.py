import os.path

def del_dir(dir):
    dir_list = []
    files_list = []
    for root, dirs, files in os.walk(dir):
        dir_list.append(dirs)
        files_list.append(files)
    if len(dir_list) <= 1:
        for i in files_list[0]:
            os.remove(dir+"/"+i)
        os.rmdir(dir)
        return True
    else:
        return False



print(del_dir("test_dir"))