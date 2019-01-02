import zipfile,os

k = os.getcwd()
z = zipfile.ZipFile(os.path.join(k,"Files","Zipped.zip"))
print(z.namelist())

print(z.getinfo("Solution Document.docx"))
Get_Info = z.getinfo("Solution Document.docx")
print(type(Get_Info))
print(Get_Info.file_size)
print(Get_Info.compress_size)

print("compressed file is %sx smaller" % (round(Get_Info.file_size/Get_Info.compress_size,2)))

z.extractall("C:\\Users\\edixish\\Downloads\\Temp_Zipped")
# z.extract("Solution Document.docx","C:\\Users\\edixish\\Downloads\\Temp_Zipped")
z.close()

os.chdir("C:\\Users\\edixish\\Downloads\\Temp_Zipped")
new = zipfile.ZipFile("new.zip","w")
new.write("Solution Document.docx",compress_type=zipfile.ZIP_DEFLATED)
new.close()