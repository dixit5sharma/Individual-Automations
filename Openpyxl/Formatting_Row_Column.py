import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet["A1"] = "Tall Row"
sheet["B2"] = "Wide Column"

sheet.row_dimensions[1].height = 70     # 0 or 12.75 is Minimum/Default height. 1 equals 1/72 of an inch. integer or float value between 0 and 409.
sheet.column_dimensions["B"].width = 20     # 0 or 8.43 is Minimum/Default height. 1 equals 1/72 of an inch. integer or float value between 0 and 255.

wb.save("Files\\Formatted_Row_Column.xlsx")