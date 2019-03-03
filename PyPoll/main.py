import os
import csv
import numpy as np

def getInfoCSVFile(Input):
# Read in the CSV file
    InputFileCSV = Input
    MyList = []
    with open(InputFileCSV, 'r') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')        
        csv_header = next(csvreader, None)        
        for row in csvreader:            
            MyList.append(row)

    return MyList



InputFile = "election_data.csv"
MyList = getInfoCSVFile(InputFile)

TotNumVotes = len(MyList)
CandidateListRep = [x[:][2] for x in MyList]
CandidateList = []

for x in CandidateListRep:
    if x not in CandidateList:
        CandidateList.append(x)

CandidateVotes =[]
MaxNumVotes = 0
for x in CandidateList:
    tempo = len([y for y in CandidateListRep if y ==x])  
    if tempo > MaxNumVotes:
        MaxNumVotes = tempo        
        Winner = x
    CandidateVotes.append(tempo)
  
   
CandidatePer= [x/sum(CandidateVotes) for x in CandidateVotes]
    
print(CandidateList)
print(CandidateVotes)
print(CandidatePer)

print(f'Election Results')
print(f'--------------------------------')
print(f'Total Votes: {TotNumVotes}')
print(f'--------------------------------')
for x in range(0,len(CandidateList),1):
    print(f'{CandidateList[x]} : {"{percent:.3%}".format(percent=CandidatePer[x])} ({CandidateVotes[x]})')
print(f'--------------------------------')
print(f'Winner : {Winner}')
print(f'--------------------------------')


file = open("Election.txt","w") 
 
file.write('Election Results\n')
file.write(f'--------------------------------\n')
file.write(f'Total Votes: {TotNumVotes}\n')
for x in range(0,len(CandidateList),1):
    file.write(f'{CandidateList[x]} : {"{percent:.3%}".format(percent=CandidatePer[x])} ({CandidateVotes[x]})\n')
file.write(f'--------------------------------')
file.write(f'Winner : {Winner}\n')
file.write(f'--------------------------------')

file.close() 








#print(f'Total: {TotPLChng}')
#print(f'Average Change: {AvgPLChng}')
#print(f'Greatest Increase in Profits: {MaxPLChng}')
#print(f'Greatest Decrease in Profits: {MinPLChng}')



#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:

#  Election Results
# -------------------------
# Total Votes: 3521001
#-------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

#n addition, your final script should both print the analysis to the terminal and export a text file with the results.
