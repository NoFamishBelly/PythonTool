import glob
import msvcrt
import os
from PIL import Image

# 搜索当前文件夹中的jpg
jpgFiles = glob.glob("*.jpg")
jpgCnt = len(jpgFiles)

# 开始转换
if jpgCnt > 0:
    print(f"当前文件夹有{jpgCnt}张jpg")
    for jpgFile in jpgFiles:
        jpgName = os.path.basename(jpgFile)
        pngName = jpgName.replace("jpg", "png")
        print(f"{jpgName}  ------>  {pngName}\n")
        image = Image.open(jpgName)
        image.save(pngName)
else:
    print("当前文件夹中没有jpg")

# 防止程序自行结束
print("按下任意键结束")
msvcrt.getch()
