#Import os and csv
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Open csv, set delimiter, and read header
with open(budget_data) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")

    budget_header = next(budget_reader)
    #print(budget_header)

#Calculate the total number of months included in the dataset, and sum the total profit or loss
    totalmonths = 0
    net_pl = 0

    for row in budget_reader:
        row[1] = int(row[1])
        totalmonths += 1
        net_pl = net_pl + row[1]

#Calculate the total changes in profit/losses over entire period, then find average of changes
with open(budget_data) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")
    
    prof_or_loss = [0]
    month = []
    change = [0]

    for row in budget_reader:
        if row == budget_header:
            continue
        else: prof_or_loss.append(row[1])
        month.append(row[0])
        #change = int(change)
        print(prof_or_loss)
        print(month)
    
    # for x in prof_or_loss:
    #     x = int(x)
        # change_diff = [prof_or_loss[x + 1] - prof_or_loss[x] for x in prof_or_loss]
        # change.append(change_diff)
        # print(change)

    # for i in budget_reader:
    #     if i = 1:
    #         change.append(0)
    #     else: change.append(row)

#Calculate the greatest increase in profits (date and amount) over entire period

#Calculate the greatest decrease in losses (date and amount) over entire period

#Print results
print("Financial Analysis",'\n')
print("---------------------------------",'\n')
print("Total Months: " + str(totalmonths),'\n')
print("Total: " + str(net_pl),'\n')
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")