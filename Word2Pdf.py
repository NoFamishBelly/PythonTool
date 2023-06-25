from docx2pdf import convert
import glob
import msvcrt
import os

wordFiles = glob.glob("*.docx")
wordCnt = len(wordFiles)

if wordCnt > 0:
    print(f"当前文件夹有{wordCnt}个docx文档")
    for wordFile in wordFiles:
        wordName = os.path.basename(wordFile)
        pdfName = wordName.replace("docx", "pdf")
        print(f"{wordName}  ------>  {pdfName}\n")
        convert(wordName, pdfName)
else:
    print("当前文件夹中没有docx文档")


print("按下任意键结束")
msvcrt.getch()
