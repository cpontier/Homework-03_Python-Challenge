'''
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
'''

#download more packages than you need?
import os
import csv
from collections import defaultdict
import operator

#initialize

totalvotes = 0
election_dict = {}

#read from CSV

OriginalCSV = os.path.join('raw_data','election_data_1.csv')

with open(OriginalCSV, 'r') as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader, None) #skip header

    for row in csvReader:

        if row[2] in election_dict:
            election_dict[row[2]] += 1
        else:
            election_dict[row[2]] = 1
        
        totalvotes += 1

winner = max(election_dict, key=election_dict.get)

#output the results

with open("Output.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("------------------------\n")
    text_file.write("Total Votes: %s \n" % totalvotes)
    text_file.write("------------------------\n")


    for k,v in election_dict.items():
        texttowrite = (str(k) + ' : ' + str((v/totalvotes)*100) + "% (" + str(v) + ") \n")
        text_file.write(texttowrite)
    
    
    text_file.write("Winner: " + str(winner) + "!")
