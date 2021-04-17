import os.path

def get_dir(dir, ext, fl):
    dir_list = []
    files_list = []
    for roots, dirs, files in os.walk(dir):
        if len(dirs) != 0:
            dir_list.append(dirs)
        if len(files) != 0:
            files_list.append(files)      
    ext_files = []
    directory = []
    for i in files_list[0]:
        if ext in i:
            ext_files.append(i)    
    for k in dir_list[0]:
        directory.append(k)   
    if fl == True:
        for m in files_list[1]:
            if ext in m:
                ext_files.append(m)
        for n in dir_list[1]:
            directory.append(n)        

           
    return [ext_files, directory]
