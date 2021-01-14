#Import os and csv
import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Open csv, set delimiter, and read header
with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")

    election_header = next(election_reader)

    #Print header to test code
    #print(election_header)

    #List the candidates who received votes and count the total votes
    cand_name = []
    # total_votes = []

    #Add to total number of votes if already listed
    for row in election_reader:
        if row[2] in cand_name:
            continue

    #Add new candidate if not listed, and add to total number of votes    
        else: cand_name.append(row[2])
    
    # vote_sum = sum(total_votes)
    # print(vote_sum)
  
    # #Start dictionary
    # cand_dict = {"candidates": [cand_name]}
    print(cand_name)

with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")


    #Find how many votes each candidate received
    #cand_votes = [0, 0, 0, 0]
    Khan_votes = []
    Correy_votes = []
    Li_votes = []
    Otooley_votes = []

    for row in election_reader:
        if row[2] == "Khan":
            Khan_votes.append(1)
        elif row[2] == "Correy":
            Correy_votes.append(1)
        elif row[2] == "Li":
            Li_votes.append(1)
        elif row[2] == "O'Tooley":
            Otooley_votes.append(1)

    Khan_sum = sum(Khan_votes)
    print(Khan_sum)

    Correy_sum = sum(Correy_votes)    
    print(Correy_sum)
    
    Li_sum = sum(Li_votes)
    print(Li_sum)

    Otooley_sum = sum(Otooley_votes)
    print(Otooley_sum)

    #Find the total number of votes
    Totalvotes = Khan_sum + Correy_sum + Li_sum + Otooley_sum
    print(Totalvotes)

    #Calculate the percent of votes each candidate won
    Khan_percent = Khan_sum / Totalvotes
    print(Khan_percent)

    Correy_percent = Correy_sum / Totalvotes
    print(Correy_percent)

    Li_percent = Li_sum / Totalvotes
    print(Li_percent)

    Otooley_percent = Otooley_sum / Totalvotes
    print(Otooley_percent)

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
