from io import BytesIO

from PIL import Image
import os
import time


# def generate_image(image_type, width, height, color):
#     print(image_type, width, height, color)
#
#     mode = 'RGB'
#     width = int(width)
#     height = int(height)
#
    # image = Image.new(mode, (width, height), 0)
#     width_per = height / 3
#     for x in range(0, width):
#         for y in range(0, height):
#             if x < width_per:
#                 image.putpixel((x, y),color[0] )
#             elif width_per <x < 2*width_per:
#                 image.putpixel((x, y), color[1])
#             else:
#                 image.putpixel((x, y), color[2])
#     image_dir = os.path.join('image')
#     image_name = '%sx%s_%s.%s' % (width, height, int(time.time()), image_type)
#     image_path = os.path.join(image_dir, image_name)
#
#
#     image.save(image_path)
#
#     print('image_path:%s' % (image_path))
#     return image_path
#
# generate_image('png',500,500,[(36,239,65),(250,239,65),(250,22,130)])


# def Picture_Synthesis(mother_img,
#                       son_img,
#                       save_img,
#                       coordinate=None):
#     """
#     :param mother_img: 母图
#     :param son_img: 子图
#     :param save_img: 保存图片名
#     :param coordinate: 子图在母图的坐标
#     :return:
#     """
#     #将图片赋值,方便后面的代码调用
#     M_Img = Image.open(mother_img)
#     S_Img = Image.open(son_img)
#     factor = 1
#
#     #给图片指定色彩显示格式
#     M_Img = M_Img.convert("RGBA")  # CMYK/RGBA 转换颜色格式（CMYK用于打印机的色彩，RGBA用于显示器的色彩）
#
#     # 获取图片的尺寸
#     M_Img_w, M_Img_h = M_Img.size  # 获取被放图片的大小（母图）
#     print("母图尺寸：",M_Img.size)
#     S_Img_w, S_Img_h = S_Img.size  # 获取小图的大小（子图）
#     print("子图尺寸：",S_Img.size)
#
#     size_w = int(S_Img_w / factor)
#     size_h = int(S_Img_h / factor)
#
#     # 防止子图尺寸大于母图
#     if S_Img_w > size_w:
#         S_Img_w = size_w
#     if S_Img_h > size_h:
#         S_Img_h = size_h
#
#     # # 重新设置子图的尺寸
#     # icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
#     icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
#     w = int((M_Img_w - S_Img_w) / 2)
#     h = int((M_Img_h - S_Img_h) / 2)
#
#     try:
#         if coordinate==None or coordinate=="":
#             coordinate=(w, h)
#             # 粘贴子图到母图的指定坐标（当前居中）
#             M_Img.paste(icon, coordinate, mask=None)
#         else:
#             print("已经指定坐标")
#             # 粘贴子图到母图的指定坐标（当前居中）
#             M_Img.paste(icon, coordinate, mask=None)
#     except:
#         print("坐标指定出错 ")
#     # 保存图片
#     M_Img.save(save_img)

# Picture_Synthesis('image/500x500_1604655243.png','image/logo.png', "image/test.png",(210,210))

# a = Image.open("image/500x500_1604655243.png")
# b = Image.open('image/logo.png').convert('RGBA')
# a.paste(b, (210,210),b)
# a.save('image/test.png', 'PNG', quality = 100)

def convertPixel(r, g, b, a=1):
    color = "#%02X%02X%02X" % (r, g, b)
    opacity = a
    return (color, opacity)

r = "image/test.png"
root, ext = os.path.splitext(r)

image = Image.open(r)
mode = image.mode
pixels = image.load()
width, height = image.size

# print(image.mode)
#
# if "RGB" in mode:
#     output = '<svg width="%d" height="%d" version="1.0" id="svg" viewBox="00%d%d" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink">' % (width, height, width, height)
#
#     for r in range(height):
#         for c in range(width):
#             color, opacity = convertPixel(*pixels[c, r])
#             output += '<rect x="%d" y="%d" width="1" height="1" fill=" %s" fill-opacity=" % s"/>' % (c, r, color, opacity)
#
#     output += "</svg>"
#
#     with open(root + ".svg", "w") as f:
#         f.write(output)
