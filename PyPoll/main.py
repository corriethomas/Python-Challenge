#Import os and csv
import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Open csv, set delimiter, and read header
with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")

    election_header = next(election_reader)

    #Print header to test code
    # print(election_header)

    #Find the total number of votes
    # totalcount = []

    # for row in election_reader:
    #     totalcount.append(1)

    #     vote_sum = sum(totalcount)
    # print(vote_sum)

    #List the candidates who received votes
    cand_name = []

    #Add to total number of votes if already listed
    for row in election_reader:
        if row[2] in cand_name:
            continue

        #Add new candidate if not listed, and add to total number of votes    
        else: cand_name.append(row[2])
        
    print(cand_name)

    #Find how many votes each candidate received
    Khan_votes = []
    Correy_votes = 0
    Li_votes = 0
    Otooley_votes = 0
    
    for row in election_reader:
        if row[2] == 'Khan':
            Khan_votes.append(1)

    print(Khan_votes)


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
