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

    #Calculate and format the percent of votes each candidate won
    Khan_percent = Khan_sum / Totalvotes
    kpercent = "{:.3%}".format(Khan_percent)
    print(kpercent)

    Correy_percent = Correy_sum / Totalvotes
    cpercent = "{:.3%}".format(Correy_percent)
    print(cpercent)

    Li_percent = Li_sum / Totalvotes
    lpercent = "{:.3%}".format(Li_percent)
    print(lpercent)

    Otooley_percent = Otooley_sum / Totalvotes
    opercent = "{:.3%}".format(Otooley_percent)
    print(opercent)

    #Create dictionary to store candidate name and votes in one place
    cand_dict = {}
    cand_dict = {"Name": cand_name, "Votes": [Khan_sum, Correy_sum, Li_sum, Otooley_sum]}
    print(cand_dict)

with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")     

    #Find the winner based on popular votes
    winner_votes = max(cand_dict["Votes"])
    winner = str

    if winner_votes == Khan_sum:
        winner = cand_dict["Name"][0]
    elif winner_votes == Correy_sum:
        winner = cand_dict["Name"][1]
    elif winner_votes == Li_sum:
        winner = cand_dict["Name"][2]
    elif winner_votes == Otooley_sum:
        winner = cand_dict["Name"][3]
    print(winner)

    #Print the analysis
    print("Election Results")
    print("----------------------")
    print("Total Votes: ")
    print("----------------------")
    #print candidates
    print("----------------------")
    print("Winner: ")
    print("----------------------")
