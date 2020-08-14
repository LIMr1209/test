from color_name import HexNameDict, color_name_zh
from color_numpy import RGB
from scipy import spatial

rgb_list = [[229, 237, 240],
            [63, 71, 77],
            [123, 142, 152],
            [179, 188, 194],
            [226, 227, 234],
            [165, 171, 180],
            [153, 85, 123],
            [70, 71, 93],
            [47, 42, 37],
            [207, 206, 205],
            [160, 149, 136],
            [131, 109, 83],
            [197, 197, 194],
            [248, 248, 248],
            [18, 162, 128],
            [156, 83, 66],
            [168, 64, 62],
            [230, 234, 239],
            [241, 245, 249],
            [254, 254, 254],
            [104, 104, 104],
            [18, 16, 17],
            [144, 140, 136],
            [69, 68, 69],
            [122, 117, 85],
            [243, 234, 231],
            [205, 192, 183],
            [253, 253, 251],
            [124, 118, 122],
            [181, 180, 181],
            [253, 253, 253],
            [68, 24, 52],
            [132, 157, 124],
            [250, 251, 250],
            [250, 246, 158],
            [193, 193, 187],
            [242, 222, 190],
            [187, 151, 107],
            [39, 30, 22],
            [94, 86, 91],
            [227, 213, 192],
            [156, 109, 88],
            [158, 174, 176],
            [250, 233, 210],
            [111, 97, 88],
            [223, 221, 215],
            [206, 170, 136],
            [231, 199, 169],
            [63, 33, 23],
            [203, 151, 101],
            [199, 40, 10],
            [137, 115, 73],
            [181, 178, 163],
            [220, 228, 234],
            [203, 204, 200],
            [95, 98, 96],
            [24, 26, 23],
            [154, 156, 153],
            [201, 153, 129],
            [75, 58, 43],
            [138, 101, 80],
            [150, 152, 156],
            [180, 181, 183],
            [132, 99, 31],
            [241, 242, 242],
            [169, 124, 92],
            [210, 203, 213],
            [233, 173, 88],
            [233, 192, 158],
            [151, 170, 169],
            [58, 71, 72],
            [174, 190, 189],
            [209, 219, 220],
            [237, 240, 236],
            [80, 120, 53],
            [193, 200, 195],
            [252, 252, 250],
            [165, 170, 170],
            [104, 107, 107],
            [212, 214, 214],
            [250, 250, 250],
            [153, 107, 84],
            [208, 156, 126],
            [175, 166, 177],
            [212, 200, 206],
            [253, 252, 252],
            [12, 16, 16],
            [68, 76, 53],
            [228, 178, 79],
            [99, 136, 155],
            [229, 228, 229],
            [205, 205, 207],
            [172, 175, 179],
            [118, 102, 70],
            [166, 144, 101],
            [204, 204, 203],
            [177, 179, 179],
            [251, 251, 251],
            [47, 59, 60],
            [13, 17, 18], ]
a = spatial.KDTree(RGB)  # K近邻算法
for pt in rgb_list:
    b = a.query(pt)

    NearestRGB = (RGB[spatial.KDTree(RGB).query(pt)[1]])

    s = '#' + format(NearestRGB[0], 'x').zfill(2) + format(NearestRGB[1], 'x').zfill(2) + format(NearestRGB[2],
                                                                                                 'x').zfill(
        2)
    ColorHex = s.upper()  # "#8B7355"  # "#8B7355"
    ColorDiff = '(' + '{0:+d}'.format(NearestRGB[0] - pt[0]) + ',' + '{0:+d}'.format(
        NearestRGB[1] - pt[1]) + ',' + '{0:+d}'.format(NearestRGB[2] - pt[2]) + ')'
    try:
        ColorName = HexNameDict[ColorHex]
        chines_name = color_name_zh[ColorHex]
    except:
        ColorName = "not found"
    print('RGB ' + str(pt) + ' 英文颜色名称:' + ColorName + ' 中文颜色名称:' + chines_name + '   偏离RGB' + str(
        NearestRGB) + ', 偏离' + ColorDiff + '.')