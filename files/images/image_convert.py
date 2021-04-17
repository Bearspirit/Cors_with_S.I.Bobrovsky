import os.path
from PIL import Image, ImageDraw, ImageColor
from files_dir_lists import get_dir

def convert_image(ext_1, ext_2):
    fl_list = get_dir(".", ext_1, False)
    for im in fl_list[0]:
        pic = Image.open(im)
        s = im.rstrip(ext_1)
        pic.save(s+ext_2)
    return os.path.isfile(s+ext_2)


print(convert_image(".jpg", ".png"))