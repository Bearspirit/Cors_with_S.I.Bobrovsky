import os.path
from PIL import Image, ImageDraw, ImageColor
from files_dir_lists import get_dir

def convert_image(ext_1, ext_2):
    fl_list = get_dir(".", ext_1, False)
    for im in fl_list[0]:
        pic = Image.open(im)
        draw = ImageDraw.Draw(pic)
        sz = pic.size
        draw.rectangle([sz[0]/2-30,sz[1]/2-30, sz[0]/2+30, sz[1]/2+30], outline=(255,0,0), width=3)
        draw.multiline_text((sz[0]/2-15,sz[1]/2-15), "Hello,\nWorld!", fill=(0,0,0))
        s = im.rstrip(ext_1)
        pic.save(s+ext_2)
        del draw
    return os.path.isfile(s+ext_2)

print(convert_image(".jpg", ".png"))