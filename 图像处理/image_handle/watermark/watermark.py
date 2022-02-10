from PIL import Image
import os


def watermark(image_path, new_image_path, size):

    image = Image.open(image_path)
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    for x in range(0, width):
        for y in range(0, height):
            if x <= size[0][1] and x >= size[0][0] and y <= size[1][1] and y >= size[1][0]:
                pix[x, y] = (255,255,255)
    image.save(new_image_path)



if __name__ == '__main__':
    path = "C:\\Users\\thn\\Desktop\\origin_images"
    new_path = "C:\\Users\\thn\\Desktop\\new_images"
    size = [[0,100],[0,100]] # 限制修改 像素

    for i, j in enumerate(os.listdir(path)):
        try:
            image_path = os.path.join(path, j)
            new_image_path = os.path.join(new_path, j)
            watermark(image_path, new_image_path, size)  # 保存图片
        except:
            continue
