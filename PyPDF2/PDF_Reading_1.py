import PyPDF2

pdfObj = open("Files\\meetingminutes.pdf","rb")     # Reading in binary mode
pdfReader = PyPDF2.PdfFileReader(pdfObj)
print(pdfReader.numPages)       # Number of Pages

pageObj = pdfReader.getPage(0)      # Zero based indexing
print(pageObj.extractText())
pdfObj.close()