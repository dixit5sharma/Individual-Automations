import csv

fileObj = open("FIles\\example.csv")
csvReader = csv.reader(fileObj)
# print(list(csvReader))        # If this is executed, below will not work since it is cursor based.

for each in csvReader:
    print("row#"+str(csvReader.line_num),str(each))     # csvReader Object has line_num method returning row (int)
fileObj.close()