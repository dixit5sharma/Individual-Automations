import PyPDF2

pdfObj = open("Files\\meetingminutes.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfObj)
pageObj = pdfReader.getPage(0)

""" rotateClockwise() and rotateCounterClockwise() """
pageObj.rotateClockwise(90)     # Multiple of 90 - 90, 180, 270....

rotatedPDF = PyPDF2.PdfFileWriter()
rotatedPDF.addPage(pageObj)
newPDF = open("Files\\rotated.pdf","wb")
rotatedPDF.write(newPDF)

newPDF.close()
pdfObj.close()