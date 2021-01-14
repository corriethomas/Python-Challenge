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

    #List the candidates who received votes and count the total votes
    cand_name = []
    total_votes = []
    
    #Add to total number of votes if already listed
    for row in election_reader:
        if row[2] in cand_name:
            total_votes.append(1)

        #Add new candidate if not listed, and add to total number of votes    
        else: cand_name.append(row[2]) and total_votes.append(1)
        
    vote_sum = sum(total_votes)
    print(vote_sum)

    #Start dictionary
    cand_dict = {"candidates": [cand_name]}
    print(cand_dict)
    
    #Find how many votes each candidate received
    
    # for row in election_reader:
    #     if row[2] == "Khan":
    #         Khan_votes = Khan_votes + 1
    #     elif row[2] == "Correy":
    #         Correy_votes == Correy_votes + 1
    #     elif row[2] == "Li":
    #         Li_votes == Li_votes + 1
    #     elif row[2] == "O'Tooley":
    #         Otooley_votes == Otooley_votes + 1
    
    # print(Khan_votes)
    # print(Correy_votes)
    # print(Li_votes)
    # print(Otooley_votes)


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
