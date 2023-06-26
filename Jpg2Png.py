import glob
import msvcrt
import os
from PIL import Image

# 搜索当前文件夹中的jpg
jpg_files = glob.glob("*.jpg")
jpg_cnt = len(jpg_files)

# 开始转换
if jpg_cnt > 0:
    print(f"当前文件夹有{jpg_cnt}张jpg")
    for jpg_file in jpg_files:
        jpg_name = os.path.basename(jpg_file)
        png_name = jpg_name.replace("jpg", "png")
        print(f"{jpg_name}  ------>  {png_name}\n")
        image = Image.open(jpg_name)
        image.save(png_name)
else:
    print("当前文件夹中没有jpg")

# 防止程序自行结束
print("按下任意键结束")
msvcrt.getch()
