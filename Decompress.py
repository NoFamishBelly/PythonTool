import glob
import msvcrt
import os
import zipfile
import rarfile
import py7zr
from unidecode import unidecode
import patoolib


# 解压zip
def decompress_zip(zip_file_name, decompress_file_name):
    with zipfile.ZipFile(zip_file_name, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            # try:
            #     file_info.filename = file_info.filename.encode('cp437').decode('utf-8')
            #     # file_info.filename = unidecode(file_info.filename)
            # except UnicodeDecodeError:
            #     file_info.filename = file_info.filename.encode('cp437').decode('gbk')
            print(f"decompress --- {file_info.filename}")
            zip_ref.extract(file_info, decompress_file_name)


# 解压7z
def decompress_7z(seven_z_file_name, decompress_file_name):
    with py7zr.SevenZipFile(seven_z_file_name, "r") as seven_z_archive:
        seven_z_archive.extractall(decompress_file_name)
        # files = seven_z_archive.list()
        # for file_info in files:
        #     file_name = file_info.filename
        #     print(f"decompress --- {file_name}")
        #     seven_z_archive.extract(decompress_file_name)


# 解压rar
def decompress_rar(rar_file_name, decompress_file_name):
    with rarfile.RarFile(rar_file_name, "r") as rar_ref:
        for file_info in rar_ref.infolist():
            # try:
            #     file_info.filename = file_info.filename.encode('cp437').decode('utf-8')
            # except UnicodeDecodeError:
            #     file_info.filename = file_info.filename.encode('cp437').decode('gbk')
            print(f"decompress --- {file_info.filename}")
            rar_ref.extract(file_info, decompress_file_name)


# 搜索当前文件中的zip/rar
compress_files = glob.glob("*.zip") + glob.glob("*.7z") + glob.glob("*.rar")
compress_cnt = len(compress_files)


# 解压文件名
def get_decompress_name(temp_compress_name):
    if temp_compress_name.endswith(".zip"):
        return temp_compress_name.replace(".zip", "")
    elif temp_compress_name.endswith(".7z"):
        return temp_compress_name.replace(".7z", "")
    else:
        return temp_compress_name.replace(".rar", "")


# 开始解压
if compress_cnt > 0:
    print(f"当前文件夹有{compress_cnt}个压缩文件(zip/rar/7z)")
    for compress_file in compress_files:
        compress_name = os.path.basename(compress_file)
        decompress_name = get_decompress_name(compress_name)
        print(f"{compress_name}  ------>  {decompress_name}")
        print("解压中, 请等待......")
        if compress_name.endswith(".zip"):
            # zip
            decompress_zip(compress_name, decompress_name)
            print("解压完毕\n\n按下任意键结束")
        elif compress_name.endswith(".7z"):
            # 7z
            decompress_7z(compress_name, decompress_name)
            print("解压完毕\n\n按下任意键结束")
        else:
            # rar
            decompress_rar(compress_name, decompress_name)
            # patoolib.extract_archive(compress_name, decompress_name)
            print("解压完毕\n\n按下任意键结束")
else:
    print("当前文件夹中没有zip/rar文档\n")
    print("按下任意键结束")

# 防止程序自行结束
msvcrt.getch()
