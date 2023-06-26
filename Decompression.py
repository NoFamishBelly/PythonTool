import glob
import msvcrt
import os
import zipfile
import rarfile


# 解压zip
def decompress_zip(zip_file_name, decompress_file_name):
    with zipfile.ZipFile(zip_file_name, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            try:
                file_info.filename = file_info.filename.encode('cp437').decode('utf-8')
            except UnicodeDecodeError:
                file_info.filename = file_info.filename.encode('cp437').decode('gbk')
            zip_ref.extract(file_info, decompress_file_name)


# 解压rar
def decompress_rar(rar_file_name, decompress_file_name):
    with rarfile.RarFile(rar_file_name, "r") as rar_ref:
        for file_info in rar_ref.infolist():
            try:
                file_info.filename = file_info.filename.encode('cp437').decode('utf-8')
            except UnicodeDecodeError:
                file_info.filename = file_info.filename.encode('cp437').decode('gbk')
        rar_ref.extract(decompress_file_name)


# 搜索当前文件中的zip/rar
compress_files = glob.glob("*.zip") + glob.glob("*.rar")
compress_cnt = len(compress_files)

# 开始解压
if compress_cnt > 0:
    print(f"当前文件夹有{compress_cnt}个压缩文件(zip/rar)")
    for compress_file in compress_files:
        compress_name = os.path.basename(compress_file)
        decompress_name = compress_name.replace(".zip", "") if compress_name.endswith(".zip") else compress_name.replace(
            ".rar", "")
        print(f"{compress_name}  ------>  {decompress_name}")
        if compress_name.endswith(".zip"):
            # zip
            decompress_zip(compress_name, decompress_name)
        else:
            # rar
            decompress_rar(compress_name, decompress_name)
else:
    print("当前文件夹中没有zip/rar文档")

# 防止程序自行结束
print("按下任意键结束")
msvcrt.getch()
