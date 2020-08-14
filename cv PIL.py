from PIL import Image

# im = Image.open('test.jpg')

#print(im.format)  # 图片格式
# print(im.size) # 图像像素尺寸 元祖
# print(im.info)  #
# im.rotate(45).show() # 图像旋转并显示
# im.save('kk.png','png') # 保存为png格式
# im = Image.new("RGB", (512, 512), "white")  # 创建新图片  white 不填默认黑
# Image.blend(image1,image2, alpha)
# 使用给定的两张图像及透明度变量alpha，插值出一张新的图像。这两张图像必须有一样的尺寸和模式。
# 如果变量alpha为0.0，将返回第一张图像的拷贝。如果变量alpha为1.0，将返回第二张图像的拷贝。对变量alpha的值没有限制。
# Image.composite(image1,image2, mask) ⇒ image
# 使用给定的两张图像及mask图像作为透明度，插值出一张新的图像。变量mask图像的模式可以为“1”，“L”或者“RGBA”。所有图像必须有相同的尺寸
# Image.eval(image,function) #：使用变量function对应的函数（该函数应该有一个参数）处理变量image所代表图像中的每一个像素点
# im.copy()  拷贝图像 不对原图像发生改变
# print(list(im.getdata())) # 每一像素点的rgb值
# print(im.getextrema()) # 该方法返回了R/G/B三个通道的最小和最大值的2元组。
# im.paste(image,box) 粘贴图片
# 将一张图粘贴到另一张图像上。变量box或者是一个给定左上角的2元组，或者是定义了左，上，右和下像素坐标的4元组，或者为空（与（0，0）一样）。如果给定4元组，被粘贴的图像的尺寸必须与区域尺寸一样。
# 如果模式不匹配，被粘贴的图像将被转换为当前图像的模式。
# im.thumbnail((100,100)) # 缩略图
# print(im.mode) # 获取图像的模式
# print(im.getpixel((4,4))) # 获取某个像素位置的值,如果图像为多通道，则返回一个元组。
# print(im.getbands()) # 获取图像的模式
# im1 = im.convert('CMYK')  # 图像转换为CMYK模式
# print(im1.mode) # 获取图像的模式
# print(im1.getpixel((4,4))) # 获取某个像素位置的值
# print(im1.getbands()) # 获取图像的模式
# r,g,b=im.split()#分割成三个通道，此时r,g,b分别为三个图像对象。
# r.show()
# g.show()
# b.show()
# im2=Image.merge("RGB",(b,g,r))#将b,r两个通道进行翻转合并
# im2.show()
# print(im.getcolors(im.size[0]*im.size[1]))

# im1 = im.convert('CMYK')
# print(im1.mode)
# print(im1.getcolors(im.size[0]*im.size[1]))

# #导入cv模块
# import cv2 as cv
# #读取图像，支持 bmp、jpg、png、tiff 等常用格式
# img = cv.imread("hehe.jpg")
# #创建窗口并显示图像
# cv.namedWindow("Image")
# cv.imshow("Image",img)
# cv.waitKey(0)
# #释放窗口
# cv.destroyAllWindows()

im = Image.new('RGB', (512, 512),'#B1B2B7')
print(im.getcolors(im.size[0]*im.size[1]))
im1 = im.convert('CMYK')
print(im1.getcolors(im1.size[0]*im1.size[1]))
