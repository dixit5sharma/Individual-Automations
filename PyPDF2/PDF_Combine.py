import PyPDF2

pdfObj1 = open("Files\\meetingminutes.pdf","rb")
pdfObj2 = open("Files\\meetingminutes2.pdf","rb")
pdfReader1 = PyPDF2.PdfFileReader(pdfObj1)
pdfReader2 = PyPDF2.PdfFileReader(pdfObj2)

combinePDF = PyPDF2.PdfFileWriter()

for i in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(i)
    combinePDF.addPage(pageObj)

for i in range(pdfReader2.numPages):
    pageObj = pdfReader2.getPage(i)
    combinePDF.addPage(pageObj)     # addPage(PageObject) adds the page to the PDFFileWriter Object

pdfOutput = open("Files\\combineMinutes.pdf","wb")
combinePDF.write(pdfOutput)
pdfOutput.close()
pdfObj1.close()
pdfObj2.close()
