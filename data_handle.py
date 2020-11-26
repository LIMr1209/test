import os

import cv2


def process_image(img, min_side):
    size = img.shape
    h, w = size[0], size[1]
    # 长边缩放为min_side
    scale = max(w, h) / float(min_side)
    new_w, new_h = int(w / scale), int(h / scale)
    resize_img = cv2.resize(img, (new_w, new_h))
    # 填充至min_side * min_side
    if new_w % 2 != 0 and new_h % 2 == 0:
        top, bottom, left, right = (min_side - new_h) / 2, (min_side - new_h) / 2, (min_side - new_w) / 2 + 1, (
                    min_side - new_w) / 2
    elif new_h % 2 != 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side - new_h) / 2 + 1, (min_side - new_h) / 2, (min_side - new_w) / 2, (
                    min_side - new_w) / 2
    elif new_h % 2 == 0 and new_w % 2 == 0:
        top, bottom, left, right = (min_side - new_h) / 2, (min_side - new_h) / 2, (min_side - new_w) / 2, (
                    min_side - new_w) / 2
    else:
        top, bottom, left, right = (min_side - new_h) / 2 + 1, (min_side - new_h) / 2, (
                    min_side - new_w) / 2 + 1, (min_side - new_w) / 2
    pad_img = cv2.copyMakeBorder(resize_img, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,
                                 value=[255, 255, 255])  # 从图像边界向上,下,左,右扩的像素数目

    return pad_img


if __name__ == '__main__':
    path = "C:\\Users\\aaa10\\Desktop\\lgx_front"
    for i, j in enumerate(os.listdir(path)):
        try:
            image = cv2.imread(path + '\\' + j)
            img_new = process_image(image, 512)
            cv2.imwrite("C:\\Users\\aaa10\\Desktop\\lgx_front_new\\"+str(i)+'.jpg',img_new)  # 保存图片
        except:
            continue