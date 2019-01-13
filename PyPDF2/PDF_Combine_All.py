#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF

import PyPDF2, os

cwd = os.getcwd()
filesPath = os.path.join(cwd,"Files")
listpdf = os.listdir(filesPath)

pdfWriter = PyPDF2.PdfFileWriter()

pdfSortedList = []
for each in listpdf:
    if each.endswith(".pdf"):
        pdfSortedList.append(each)
pdfSortedList.sort(key=str.lower)

for each in pdfSortedList:
    reading = open("Files\\"+each,"rb")
    pdfReader = PyPDF2.PdfFileReader(reading)
    if pdfReader.isEncrypted:
        continue
    else:
        for i in range(1,pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(i))

with open("Files\\CombineAllPDF.pdf","wb") as abc:
    pdfWriter.write(abc)

""" pdfFile needs to be available and open when the pdfWriter finally writes out, otherwise it cannot 
access the pages to write the new file """