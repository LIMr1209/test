import random

import cv2
from PIL import Image

# 旋转后相似度计算
def is_existed(img_all, img, semilar=0.9):
    '''
    在img_all中寻找img，当相似度到达semilar时停止
    参数：
        img_all:
        img:
        semilar：相似度阀值
    返回：    (maxValue, maxLoc, Angle)
        maxValue: 相似度- 0：不相识，1：全相似
        maxLoc：最相似的位置（x，y）
        Angle：转换到最相似的旋转角度
    '''
    if semilar <0 or semilar >1:
        semilar = 0.9

    max_val = 0  # 相似度
    # 取决于matchTemplate的最后一个参数，对于多数方法，越大越好；对于有2个方法，越小越好）
    angle = 0  # 旋转角度
    max_loc = (0,0)
    h, w = img.shape[:2]
    step = 10
    start = 0
    stop = 360
    while True:
        if step < 1:
            break
        max_val = 0
        while start < stop:
            matRotate = cv2.getRotationMatrix2D((h * 0.5, w * 0.5), -start, 1)
            dst = cv2.warpAffine(img, matRotate, (h, w))
            result = cv2.matchTemplate(
                img_all, dst, cv2.TM_CCOEFF_NORMED)
            min_max_loc = cv2.minMaxLoc(result)  # 匹配程度最大的左上角位置 (x,y)
            if min_max_loc[1] > max_val:
                max_val = min_max_loc[1]
                max_loc = min_max_loc[3]
                angle = start
                # print(f'匹配度 = {max_val}, 旋转角度 = {i}')
                if max_val >= semilar:  # 很高的匹配度，认为已经ok了
                    break
            start += step
        start = angle - step + step * 0.1
        stop = angle + step
        step = step * 0.1

    return (max_val, max_loc, angle)


img = Image.open('1.jpg')
rate = random.randint(30, 330)
print(rate)
img = img.rotate(rate)
img.save('2.jpg')


img_all = cv2.imread('1.jpg')
img = cv2.imread('2.jpg')

h, w = img.shape[:2]
levels = 0
while h>150:
    levels +=1
    img = cv2.pyrDown(img)
    h, w = img.shape[:2]

# 缩放img得到锁小次数，然后对img_all进行相同操作
for _ in range(levels):
    img_all = cv2.pyrDown(img_all)
print(is_existed(img_all,img))