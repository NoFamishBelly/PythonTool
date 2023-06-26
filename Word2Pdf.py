import glob
import msvcrt
import os
from docx2pdf import convert

# 搜索当前文件夹中的docx/doc
word_files = glob.glob("*.docx") + glob.glob("*.doc")
word_cnt = len(word_files)

# 开始转换
if word_cnt > 0:
    print(f"当前文件夹有{word_cnt}个word文档(docx/doc)")
    for word_file in word_files:
        word_name = os.path.basename(word_file)
        pdf_name = word_name.replace(".docx", ".pdf") if word_name.endswith(".docx") else word_name.replace(".doc", ".pdf")
        print(f"{word_name}  ------>  {pdf_name}\n")
        print("转换中, 请等待......")
        convert(word_name, pdf_name)
        print("转换完毕\n\n按下任意键结束")
else:
    print("当前文件夹中没有docx/doc文档\n")
    print("按下任意键结束")

# 防止程序自行结束
msvcrt.getch()
