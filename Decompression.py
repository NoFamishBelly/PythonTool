import glob
import msvcrt
import os
import zipfile
import rarfile


# 解压zip
def decompressZip(zipFileName, decompressFileName):
    with zipfile.ZipFile(zipFileName, "r") as zipRef:
        for fileInfo in zipRef.infolist():
            try:
                fileInfo.filename = fileInfo.filename.encode('cp437').decode('utf-8')
            except UnicodeDecodeError:
                fileInfo.filename = fileInfo.filename.encode('cp437').decode('gbk')
            zipRef.extract(fileInfo, decompressFileName)


# 解压rar
def decompressRar(rarFileName, decompressFileName):
    with rarfile.RarFile(rarFileName, "r") as rarRef:
        for fileInfo in rarRef.infolist():
            try:
                fileInfo.filename = fileInfo.filename.encode('cp437').decode('utf-8')
            except UnicodeDecodeError:
                fileInfo.filename = fileInfo.filename.encode('cp437').decode('gbk')
        rarRef.extract(decompressFileName)


# 搜索当前文件中的zip/rar
compressFiles = glob.glob("*.zip") + glob.glob("*.rar")
compressCnt = len(compressFiles)

# 开始解压
if compressCnt > 0:
    print(f"当前文件夹有{compressCnt}个压缩文件(zip/rar)")
    for compressFile in compressFiles:
        compressName = os.path.basename(compressFile)
        decompressName = compressName.replace(".zip", "") if compressName.endswith(".zip") else compressName.replace(
            ".rar", "")
        print(f"{compressName}  ------>  {decompressName}")
        if compressName.endswith(".zip"):
            # zip
            decompressZip(compressName, decompressName)
        else:
            # rar
            decompressRar(compressName, decompressName)
else:
    print("当前文件夹中没有zip/rar文档")

# 防止程序自行结束
print("按下任意键结束")
msvcrt.getch()
