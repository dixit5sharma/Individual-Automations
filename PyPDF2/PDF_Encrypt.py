import PyPDF2

pdfObj = open("Files\\meetingminutes.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfObj)

pdfWriter = PyPDF2.PdfFileWriter()
for i in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(i))

pdfWriter.encrypt("rosemary")
""" PDFs can have a user password (allowing you to view the PDF) and an owner password (allowing you to set 
permissions for printing, commenting, extracting text, and other features). The user password and owner password
are the first and second arguments to encrypt(), respectively. If only one string argument is passed to encrypt(),
it will be used for both passwords. """

openPDF = open("Files\\PythonEncrypted.pdf","wb")
pdfWriter.write(openPDF)

openPDF.close()
pdfObj.close()