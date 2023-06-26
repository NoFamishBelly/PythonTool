import msvcrt
import zipfile
import py7zr
import os

input_folder_path = input("输入文件路径进行压缩: ")
input_compress_format = input("输入压缩格式(zip/7z): ")


# 压缩为zip
def compress_zip(folder_path, compress_file_name):
    with zipfile.ZipFile(compress_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"compress --- {file_path}")
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


# 压缩为7z
def compress_7z(folder_path, compress_file_name):
    with py7zr.SevenZipFile(compress_file_name, 'w') as seven_z_f:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"compress --- {file_path}")
                seven_z_f.write(file_path, os.path.relpath(file_path, folder_path))


# 开始压缩
if len(input_folder_path) > 0:
    if len(input_compress_format) > 0:
        if input_compress_format == "zip":
            zip_file_name = "compress_file.zip"
            print(f"{input_folder_path}中的文件被压缩至{zip_file_name}")
            print("压缩中, 请等待......")
            compress_zip(input_folder_path, zip_file_name)
            print("压缩完毕\n\n按下任意键结束")
        elif input_compress_format == "7z":
            seven_z_file_name = "compress_file.7z"
            print(f"{input_folder_path}中的文件被压缩至{seven_z_file_name}")
            print("压缩中, 请等待......")
            compress_7z(input_folder_path, seven_z_file_name)
            print("压缩完毕\n\n按下任意键结束")
        else:
            print("输入的不是zip或7z格式，无法压缩\n")
            print("按下任意键结束")

# 防止程序自行结束
msvcrt.getch()
