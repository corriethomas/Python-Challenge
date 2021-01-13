#Import os and csv
import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Open csv, set delimiter, and read header
with open(election_data) as election_csv:
    election_reader = csv.reader(election_csv, delimiter=",")

    election_header = next(election_reader)

#Print header to test code
#print(election_header)

#Find the total number of votes
for row in election_data:
    totalvote = sum()

print(totalvote)

#List the candidates who received votes (Make a dictionary)



#Calculate the percent of votes each candidate won

#Calculate the total number of votes each candidate won

#Find the winner based on popular votes

#Print the analysis
print("Election Results")
print("----------------------")
print("Total Votes: ")
print("----------------------")
#print candidates
print("----------------------")
print("Winner: ")
print("----------------------")