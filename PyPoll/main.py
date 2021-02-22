#import modules
import os
import csv

#variable to count number of votes
nVotes = 0
#create an array to store candidate name and number of votes
candidateInfo = []
#variable to find the highest number of votes
highVote = ["", 0]

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
        #increase the vote count by 1
        nVotes += 1
        #get the name of the candidate on the current row
        name = row[2]
        #use a flag to see if the candidate is already on the array
        flag = False
        #check the array for the candidate
        for candidates in candidateInfo:
            #if the candidate is already on the array, add one to their vote count and flag that the name was found
            if (name == candidates[0]):
                candidates[1] += 1
                flag = True
                break
        #if the candidate name was not found in the array, add them to the array with a vote count of 1
        if flag == False:
            candidateInfo.append([name, 1])

#print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes:", nVotes)
print("-------------------------")
#iterate over candidtates and print name, calculation of percentage of total votes, and total number of votes
for candidates in candidateInfo:
    print(candidates[0] + ": " + str(round((100 * candidates[1] / nVotes),3)) + "% (" + str(candidates[1]) + ")")
    #during iteration, find the candidate with the highest number of votes
    if candidates[1] > highVote[1]:
            highVote = candidates
print("-------------------------")
print("Winner:", highVote[0])
print("-------------------------")