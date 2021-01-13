#Import os and csv
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Open csv, set delimiter, and read header
with open(budget_data) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")

    budget_header = next(budget_reader)

#Calculate the total number of months included in the dataset

#Calculate the total amount of profit/losses over entire period

#Calculate the total changes in profit/losses over entire period, then find average of changes

#Calculate the greatest increase in profits (date and amount) over entire period

#Calculate the greatest decrease in losses (date and amount) over entire period


#Print header to test code
#print(budget_header)

#Print results
print("Financial Analysis")
print("---------------------------------")
print("Total Months: ")
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")