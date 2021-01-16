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

    Correy_sum = sum(Correy_votes)    
    
    Li_sum = sum(Li_votes)

    Otooley_sum = sum(Otooley_votes)

    #Find the total number of all votes
    Totalvotes = Khan_sum + Correy_sum + Li_sum + Otooley_sum

    #Calculate and format the percent of votes each candidate won
    Khan_percent = Khan_sum / Totalvotes
    kpercent = "{:.3%}".format(Khan_percent)

    Correy_percent = Correy_sum / Totalvotes
    cpercent = "{:.3%}".format(Correy_percent)

    Li_percent = Li_sum / Totalvotes
    lpercent = "{:.3%}".format(Li_percent)

    Otooley_percent = Otooley_sum / Totalvotes
    opercent = "{:.3%}".format(Otooley_percent)

    #Create dictionary to store candidate name and votes in one place
    cand_dict = {}
    cand_dict = {"Name": cand_name, "Votes": [Khan_sum, Correy_sum, Li_sum, Otooley_sum]}

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

    #Print the analysis in the terminal
    print('\n',"Election Results")
    print("----------------------")
    print("Total Votes: " + str(Totalvotes))
    print("----------------------")
    print(f'{cand_dict["Name"][0]}: ' + str(kpercent) + ' (' + str(Khan_sum) + ')' '\n' 
    f'{cand_dict["Name"][1]}: ' + str(cpercent) + ' (' + str(Correy_sum) + ')' '\n'
    f'{cand_dict["Name"][2]}: ' + str(lpercent) + ' (' + str(Li_sum) + ')' '\n'
    f'{cand_dict["Name"][3]}: ' + str(opercent) + ' (' + str(Otooley_sum) + ')') 
    print("----------------------")
    print("Winner: " + winner)
    print("----------------------" '\n')

#Open results text file
file = os.path.join("Analysis", "PyPoll_Results.txt")
with open(file, 'w') as text:
    
    #Set variables to be printed
    election_results = ('Election Results\n')
    space = ('----------------------\n')
    total_votes = (('Total Votes: ' + str(Totalvotes)  + '\n'))
    cand_votes = (f'{cand_dict["Name"][0]}: ' + str(kpercent) + ' (' + str(Khan_sum) + ')' '\n' 
    f'{cand_dict["Name"][1]}: ' + str(cpercent) + ' (' + str(Correy_sum) + ')' '\n'
    f'{cand_dict["Name"][2]}: ' + str(lpercent) + ' (' + str(Li_sum) + ')' '\n'
    f'{cand_dict["Name"][3]}: ' + str(opercent) + ' (' + str(Otooley_sum) + ')' + '\n')
    winner_line = ('Winner: ' + str(winner) + '\n')

    #Print/write to text file
    text.write(election_results)
    text.write(space)
    text.write(total_votes)
    text.write(space)
    text.write(cand_votes)
    text.write(space)
    text.write(winner_line)
    text.write(space)
    text.close()