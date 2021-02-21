#import modules
import os
import csv

#create variables for calculations over iteratations of the csv file
nMonths = int(0)
profitLoss = int()
netTotalPL = int(0)
aveChangePL = float()
maxIncreaseMonth = str()
maxIncrease = int(0)
maxDecreaseMonth = str()
maxDecrease = int(0)

#get csv data filepath
inputFilepath = "/Users/adamburstyn/Desktop/UM_Data_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv"
#open the csv file
with open(inputFilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip over the header
    next(csvreader)
    #cycle through the rows in the csv file
    for row in csvreader:
        #calculate total number of months
        nMonths += 1
        #calculate net total of Profits/Losses
        profitLoss = int(row[1])
        netTotalPL += profitLoss
#output results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", nMonths)
print("Total: $" + str(netTotalPL))
        
