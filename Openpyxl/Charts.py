import openpyxl

wb = openpyxl.Workbook()
sh = wb.active
for i in range(1,11):
    sh["A"+str(i)] = i

ch = openpyxl.chart.Reference(sh,min_col=1, min_row=1, max_col=1, max_row=10)
sr = openpyxl.chart.Series(ch,title='First series')

chObj = openpyxl.chart.BarChart()   # openpyxl.charts.LineChart(), openpyxl.charts.ScatterChart(), and openpyxl.charts.PieChart()
chObj.append(sr)

chObj.anchor = "C3"      # set the position
chObj.width = 7.94      # set the size (in centimeters, where 1 cm = 37.8 pixels)
chObj.height = 5.29

sh.add_chart(chObj)        # second argument (optional) is the location from where the chart should start
wb.save("Files\\ChartObject_1.xlsx")

"""
Unfortunately, in the current version of OpenPyXL (2.1.4), the load_workbook() function does not load charts
in Excel files. Even if the Excel file has charts, the loaded Workbook object will not include them.
If you load a Workbook object and immediately save it to the same .xlsx filename, you will effectively
remove the charts from it.
"""