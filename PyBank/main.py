#import modules
import os
import csv

#create variables for calculations over iteratations of the csv file
nMonths = int(0)
profitLoss = int()
netTotalPL = int(0)
aveChangePL = float()

prePL = int(0)
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
        #calculate changes of profit/losses and find the average

        #find greatest in profits date and ammount
        if (profitLoss > prePL) and (profitLoss - prePL > maxIncrease):
            maxIncrease = (abs(profitLoss) + abs(prePL))
            maxIncreaseMonth = row[0]
            print("MaxIn", maxIncreaseMonth, profitLoss, prePL, maxIncrease)
        if (profitLoss < prePL) and (abs(profitLoss) + abs(prePL)) > abs(maxDecrease):
            maxDecrease = ((abs(profitLoss) + abs(prePL)) * -1)
            maxDecreaseMonth = row[0]
            #print("MaxDe", maxDecreaseMonth, profitLoss, prePL, maxDecrease)
        
        prePL = profitLoss

#output results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", nMonths)
print("Total: $" + str(netTotalPL))
print("Average Change: $")
print("Greatest Increase in Profits:", maxIncreaseMonth, "($" + str(maxIncrease) + ")")
print("Greatest Decrease in Profits:", maxDecreaseMonth, "($" + str(maxDecrease) + ")")
        
