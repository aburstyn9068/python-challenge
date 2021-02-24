#import modules
import os
import csv

################################################
# Title: us_state_abbrev.py
# Author: Haque, A
# Date: 2016
# Availability: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5#file-us_state_abbrev-py
################################################
from us_state_abbrev import us_state_abbrev

id = []
firstName = []
lastName = []
dob = []
ssn = []
state = []

#get csv data filepath
inputFilepath = "../python-challenge/PyBoss/Resources/employee_data.csv"

#open the csv file
with open(inputFilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip over the header
    next(csvreader)

    #iterate over the rows to perform the necessary functions
    for row in csvreader:
        #create an array of the IDs
        id.append(row[0])
        #create an array of the first names
        firstName.append(row[1].split(" ")[0])
        #create an array of the last names
        lastName.append(row[1].split(" ")[1])
        #create an array of the DOBs in the appropriate format
        dob.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] + "/" + row[2].split("-")[0])
        #create an array of the SSNs in the appropriate format
        ssn.append("***-**-" + row[3].split("-")[2])
        #create an array of the states in the appropriate format
        state.append(us_state_abbrev[row[4]])

#organize the data into a tupule to output in the new format to a csv file
output = zip(id, firstName, lastName, dob, ssn, state)
outputSet = set(output)

header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]

#output to csv file
outputFilePath = "../python-challenge/PyBoss/analysis/analysis.csv"
with open(outputFilePath, "w", newline="") as csvout:
    writer = csv.writer(csvout)
    writer.writerow(header)
    for row in outputSet:
        writer.writerow(row)
