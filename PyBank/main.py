#import modules
import os
import csv

#create variables for calculations over iteratations of the csv file
nMonths = int(0)
profitLoss = int()
netTotalPL = int(0)
totalChange = int(0)
firstMonthPL = int()

prePL = int(0)
maxIncreaseMonth = str()
maxIncrease = int(0)
maxDecreaseMonth = str()
maxDecrease = int(0)

#get csv data filepath
inputFilepath = "/Users/adamburstyn/Desktop/UM_Data_Bootcamp/python-challenge/PyBank/Resources/budget_data.csv"
#open the csv file
with open(inputFilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip over the header
    next(csvreader)
    
    #go through first month data to not include the calculation that updates the total change in profit/loss
    firstRow = next(csvreader)
    #calculate total number of months
    nMonths += 1
    #calculate net total of Profits/Losses
    profitLoss = int(firstRow[1])
    netTotalPL += profitLoss
    #find greatest in profits date and ammount
    if (profitLoss > prePL) and (profitLoss - prePL > maxIncrease):
        maxIncrease = profitLoss - prePL
        maxIncreaseMonth = firstRow[0]
    if (profitLoss < prePL) and ((profitLoss - prePL) < maxDecrease):
        maxDecrease = profitLoss - prePL
        maxDecreaseMonth = firstRow[0]
    #store profit/loss number to refer to the previous months data in the next iteration
    prePL = profitLoss
    
    #cycle through the remaining rows in the csv file
    for row in csvreader:
        #calculate total number of months
        nMonths += 1
        #calculate net total of Profits/Losses
        profitLoss = int(row[1])
        netTotalPL += profitLoss
        #find greatest in profits date and ammount
        if (profitLoss > prePL) and (profitLoss - prePL > maxIncrease):
            maxIncrease = profitLoss - prePL
            maxIncreaseMonth = row[0]
        if (profitLoss < prePL) and ((profitLoss - prePL) < maxDecrease):
            maxDecrease = profitLoss - prePL
            maxDecreaseMonth = row[0]
        #update total change in profit/loss
        totalChange += (profitLoss - prePL)
        #store profit/loss number to refer to the previous months data in the next iteration
        prePL = profitLoss

#calculate average change in profit/loss
aveChangePL = totalChange / (nMonths - 1)

#output results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", nMonths)
print("Total: $" + str(netTotalPL))
print("Average Change: $" + str(round(aveChangePL,2)))
print("Greatest Increase in Profits:", maxIncreaseMonth, "($" + str(maxIncrease) + ")")
print("Greatest Decrease in Profits:", maxDecreaseMonth, "($" + str(maxDecrease) + ")")
        
