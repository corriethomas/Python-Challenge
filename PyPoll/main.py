#Import os and csv
import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Open csv, set delimiter, and read header
with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")

    election_header = next(election_reader)

    #Create list to store the candidates who received votes
    cand_name = []

    #Skip candidate if already listed in cand_name
    for row in election_reader:
        if row[2] in cand_name:
            continue

    #Add new candidate if not listed in cand_name 
        else: cand_name.append(row[2])
     
    print(cand_name)

with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")

    #Using the list of candidates we made, create a tracker to store how many votes each candidate received
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

    #Add all votes stored in each candidate's tracker
    Khan_sum = sum(Khan_votes)
    print(Khan_sum)

    Correy_sum = sum(Correy_votes)    
    print(Correy_sum)
    
    Li_sum = sum(Li_votes)
    print(Li_sum)

    Otooley_sum = sum(Otooley_votes)
    print(Otooley_sum)

    #Find the total number of all votes
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

    #Create dictionary to store candidate name and votes in one place
    # cand_dict = {}
    # cand_dict = {"Name": cand_name,
    # "Votes": Khan_sum, Correy_sum, Li_sum, Otooley_sum}
    # print(cand_dict)
        
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
