import glob
import msvcrt
import os
from docx2pdf import convert

# 搜索当前文件夹中的docx/doc
wordFiles = glob.glob("*.docx") + glob.glob("*.doc")
wordCnt = len(wordFiles)

# 开始转换
if wordCnt > 0:
    print(f"当前文件夹有{wordCnt}个word文档(docx/doc)")
    for wordFile in wordFiles:
        wordName = os.path.basename(wordFile)
        pdfName = wordName.replace(".docx", ".pdf") if wordName.endswith(".docx") else wordName.replace(".doc", ".pdf")
        print(f"{wordName}  ------>  {pdfName}\n")
        convert(wordName, pdfName)
else:
    print("当前文件夹中没有docx/doc文档")

# 防止程序自行结束
print("按下任意键结束")
msvcrt.getch()
