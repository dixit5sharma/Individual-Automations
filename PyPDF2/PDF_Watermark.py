import PyPDF2

pdfObj = open("Files\\meetingminutes.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfObj)
firstPageObj = pdfReader.getPage(0)

watermarkObj = open("Files\\watermark.pdf","rb")
watermarkReader = PyPDF2.PdfFileReader(watermarkObj)
watermarkFirstPage = watermarkReader.getPage(0)

firstPageObj.mergePage(watermarkFirstPage)

watermarkWrite = PyPDF2.PdfFileWriter()
watermarkWrite.addPage(firstPageObj)

for i in range(1,pdfReader.numPages):
    watermarkWrite.addPage(pdfReader.getPage(i))

openWatermark = open("Files\\WaterMarked.pdf","wb")
watermarkWrite.write(openWatermark)

openWatermark.close()
watermarkObj.close()
pdfObj.close()