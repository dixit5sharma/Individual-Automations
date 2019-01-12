import PyPDF2

pdfObj = open("Files\\encrypted.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfObj)
print(pdfReader.isEncrypted)        # Every File has this attribute (True / False)

# print(pdfReader.getPage(0))       # Gives an Error
pdfReader.decrypt("rosebud")        # Returns 1 if correct , returns 0 if wrong and rest of the code continues to fail
"NOTE : decrypt() method decrypts only the pdfReader object and not the actual file"
print(pdfReader.getPage(0))
pdfObj.close()