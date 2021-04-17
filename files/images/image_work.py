from PIL import Image, ImageDraw, ImageColor

im = Image.open("dog_1.png")
print(im.format, im.size, im.mode)

"""
draw = ImageDraw.Draw(im)
sz = im.size
draw.line([sz[0]/2,0, sz[0]/2,sz[1]], fill = (255, 128, 255))
draw.rectangle([10,10, 30,30], fill = (255,255,255))
draw.multiline_text((50,50), "11111\n55555")
im.save("test2.png", "PNG")
del draw
im.show()
"""