import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.active
Italic24Font = Font(name="Times New Roman",size=24,italic=True,bold=True)
StyleObj = NamedStyle(name="Italic24Font",font=Italic24Font)
sheet["A1"].style = StyleObj

sheet["A1"] = "Hello World"
wb.save("Files\\Style_Font_1.xlsx")