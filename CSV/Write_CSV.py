import csv

csvobj = open("Files\\Output.csv","w",newline="")      # If newline is not used, rows will be double spaced
csvWriter = csv.writer(csvobj)
csvWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])        # takes a list argument
csvWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
csvWriter.writerow([1, 2, 3.141592, 4])         # returns number of characters written to the file for that row (including newline characters)
csvobj.close()
