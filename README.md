# python-challenge
Python Coding Project

This repository contains python code to make analyses on "PyBank" "PyPoll", "PyBoss", and "PyParagraph."

PyBank reads a csv file that contains a companies financial records, and performs accounting analysis on the data.
It calculates the number of months contained in the file, the net total profits/losses, the average profit/loss, the greatest increase in profits, and the greatest decrease in losses over the time period provided.
The code outputs the information to the termial, as well as a separate file, analysis.txt.

PyPoll reads a csv file that contains polling information for an electon.
It reads the data and detrmines the total number of votes as well as a list of candidates and how many votes they recieved and their percentage of total votes.
It will also determine the winner baased on which candidate recieved the most votes.
The code outputs the information to the termial, as well as a separate file, analysis.txt.

PyBoss reads a csv file containing employee data and outputs it to a new file in an updated format. The code splits the employees name into a first and last name category, updates the date of birth from YYYY-MM-DD to MM/DD/YYYY, conseals everthing but the last 4 digits of the social security number, and changes the full state name to its abbreviation.
The final format is output in the analysis.csv file.
The conversion of the full state name to its abbreviation is done using the us_states_abbrev.py [1] dictionary.

PyParagraph analyzes a passage in a file to determine its complexity. It calls a function to read a given file path and endline indicator. The code will calculate the approximate word count, apporoximate sentence count, approximate letter count, and average sentence length. The results will be displayed on the terminal.

1. Haque, A (2016) us_state_abbrev.py [Python dictionary]. https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5#file-us_state_abbrev-py
