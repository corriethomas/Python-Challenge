#Import os and csv
import os
import csv

budget_data = os.path.join("budget_data.csv")

#Open csv, set delimiter, and read header
with open(budget_data) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")

    budget_header = next(budget_reader)
    #print(budget_header)

#Calculate the total number of months included in the dataset, and sum the total profit or loss
#Set the lists we want to store our months and profit/losses to
    totalmonths = 0
    net_pl = 0
    current_prof_or_loss = []
    previous_prof_or_loss = [0]
    change_in_prof_or_loss = []
    month = []

    for row in budget_reader:
        row[1] = int(row[1])
        totalmonths += 1
        month.append(row[0])
        net_pl = net_pl + row[1]
        current_prof_or_loss.append(row[1])
        previous_prof_or_loss.append(current_prof_or_loss[-1])
        change_in_prof_or_loss = ([current_prof_or_loss[row]-previous_prof_or_loss[row] for row in range(len(current_prof_or_loss))])
        #print(current_prof_or_loss)
        #print(previous_prof_or_loss)
        #print(change_in_prof_or_loss)

#Calculate the total changes in profit/losses over entire period, then find average of changes
    
    totalchanges = sum(change_in_prof_or_loss)
    #avgchange = totalchanges/totalmonths
    print(totalchanges)
    #print(avgchange)


#Calculate the greatest increase in profits (date and amount) over entire period

#Calculate the greatest decrease in losses (date and amount) over entire period

#Print results
print('\n',"Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(totalmonths))
print("Total: " + "$" + str(net_pl))
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: " + '\n')

#Open results text file
# results_file = os.path.join("Analysis", "PyBank_Results.txt")
# with open(results_file, 'w') as text:
#     financial_analysis = ("Financial Analysis" + '\n')
#     space = ("---------------------------------" + '\n')
#     total_months = ("Total Months: " + str(totalmonths) + '\n')
#     total_prof_or_loss = ("Total: " + "$" + str(net_pl) + '\n')
#     average_change = ("Average Change: " + '\n')
#     greatest_increase = ("Greatest Increase in Profits: " + '\n')
#     greatest_decrease = ("Greatest Decrease in Profits: " + '\n')

#     #Print/write to text file
#     text.write(financial_analysis)
#     text.write(space)
#     text.write(total_months)
#     text.write(total_prof_or_loss)
#     text.write(average_change)
#     text.write(greatest_increase)
#     text.write(greatest_decrease)