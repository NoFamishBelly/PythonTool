from PIL import Image
import glob
import msvcrt
import os

jpgFiles = glob.glob("*.jpg")
jpgCnt = len(jpgFiles)

if jpgCnt > 0:
    print(f"当前文件夹有{jpgCnt}张jpg")
    for jpgFile in jpgFiles:
        jpgName = os.path.basename(jpgFile)
        pngName = jpgName.replace("jpg", "png")
        image = Image.open(jpgName)
        image.save(pngName)
        print(f"{jpgName} 转化为 {pngName}\n")
else:
    print("当前文件夹中没有jpg")

print("按下任意键结束")
msvcrt.getch()
