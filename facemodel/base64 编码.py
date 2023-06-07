import base64

def image_to_base64(filepath):
    """
    图片转base64
    """
    file_type = filepath.rsplit(".",1)[1]
    with open(filepath, "rb") as image_file:
        # 读取图片数据并进行 Base64 编码
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f'data:image/{file_type};base64,' + encoded_string

def base64_to_image(base64_img, path):
    prefix = base64_img.split(",")[0]
    if "png" in prefix:
        path += ".png"
    elif "jpg" in prefix:
        path += ".jpg"
    elif "jpeg" in prefix:
        path += ".jpeg"
    encoded_string = base64_img.split(",")[1]
    # 将 Base64 编码字符串解码为图像数据
    decoded_data = base64.b64decode(encoded_string)
    # 将图像数据写入到文件中
    with open(path, "wb") as image_file:
        image_file.write(decoded_data)

base64_to_image(image_to_base64("/home/limr/Desktop/图片/20230509-173935.png"), "./test.png")
