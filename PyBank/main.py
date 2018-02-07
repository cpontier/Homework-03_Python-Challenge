import os
import csv

'''
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
'''

#Variables that I need to calculate

nMonths = 0
Revenue = 0
RevChng = 0
RevChngRow = 0
AvgRevChng = 0
TotalRevChng = 0
GreatestIncrease = 0
GreatestIncreaseMonth = ""
GreatestDecrease = 0
GreatestDecreaseMonth = ""

Sheets = ['1', '2']

#store filepath in a variable

OriginalCSV = os.path.join('raw_data','budget_data_1.csv')

#read from CSV

with open(OriginalCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) #skip header

        for row in csvReader:
            nMonths += 1
            PrevRevenue = 0
            RevChng = int(row[1]) - PrevRevenue
                
            if(RevChng > 0 and RevChng > GreatestIncrease):
                GreatestIncrease = RevChng
                GreatestIncreaseMonth = (row[0])
                
            elif(RevChng < 0 and RevChng < GreatestDecrease):
                GreatestDecrease = RevChng
                GreatestDecreaseMonth = (row[0])

            Revenue = Revenue + int(row[1])
            TotalRevChng = TotalRevChng + RevChng
            PrevRevenue = int(row[1])
            
AvgRevChng = TotalRevChng / (nMonths - 1)

#output the results

with open("Output.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------\n")
    text_file.write("Total Months: %s \n" % nMonths)
    text_file.write("Total Revenue: %s \n" % Revenue)
    text_file.write("Average Revenue Change: %s \n" % AvgRevChng)
    text_file.write("Greatest Increase in Revenue: " + str(GreatestIncreaseMonth) + " " + str(GreatestIncrease))
    text_file.write("\nGreatest Decrease in Revenue: " + str(GreatestDecreaseMonth) + " " + str(GreatestDecrease))