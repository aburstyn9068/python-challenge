#import modules
import os
import csv

#variable to count number of votes
nVotes = 0
#create an array to store candidate name and number of votes
candidateInfo = []

#output file path
outputFilePath = "../python-challenge/PyPoll/analysis/analysis.txt"

#get csv data filepath
inputFilepath = "../python-challenge/PyPoll/Resources/election_data.csv"

#open the csv file
with open(inputFilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip over the header
    next(csvreader)

    #iterate the data file to find the necessary information
    for row in csvreader:
        nVotes += 1
        # name = row[2]
        # if name in candidateInfo:
        #     candidateInfo[candidateInfo.index(name)][1] += 1
        # else:
        #     candidateInfo.append([name, 1])
        # print(candidateInfo)

#print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes:", nVotes)
print("-------------------------")            
