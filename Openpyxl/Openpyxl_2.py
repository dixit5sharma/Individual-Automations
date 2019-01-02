import openpyxl

wb = openpyxl.load_workbook("Files\\example.xlsx")
print(list(wb))     # Works - wb is an iterable (list,tuple) containing WorkSheet Objects with all the Sheet names
wbSheet = wb["Sheet1"]
print(list(wbSheet))     # Works - wbSheet is also an iterable containing list of all Cell objects
# wbSheet = wb.get_active_sheet()
# print(tuple(wbSheet["A1":"C3"]))      #

for row in wbSheet["A1":"C3"]:      # Slicing - This tuple contains 3 elements - ((A1,B1,C1),(A2,B2,C2),(A3,B3,C3))
    for cell in row:        # Iterating each element of the tuple (Eg. A1,B1,C1)
        # print(type(row))  # tuple
        print("Value at Cell",cell.coordinate,"=",cell.value , end="    ")
    print()

print(list(wbSheet.columns)[1])
for eachCell in list(wbSheet.columns)[1]:
    print(eachCell.value)