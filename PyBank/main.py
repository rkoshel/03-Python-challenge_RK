# Set modules
import os
import csv
from pathlib import Path 

# Path to collect data from the Resources folder
pybankcsv = os.path.join('..', 'Resources', 'budget_data.csv')

months = []
total = []
average = []
g_increase = ""
g_decrease = ""

with open(pybankcsv, 'r') as budgetreader:

    pybankcsv = csv.reader(budgetreader, delimiter = ',')
    next(pybankcsv)

# Loop through file to add to the month and profit lists
    for row in pybankcsv:

        months.append(row[0])
        total.append(int(row[1]))
        Month_total = len(months)
        GTotal = sum(total)

    for i in range(len(total)-1):

        average.append(total[i+1]-total[i])

        # Obtain the max and min of the the montly change 

        i = 0
        for i in range (1, len(total)):

            average.append(total[i] - total[i-1])
            g_increase = max(average)
            greatest_increase_month = str(months[average.index(max(average))])
            g_decrease = min(average)
            greatest_decrease_month = str(months[average.index(min(average))])
            
# Print Statements
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(Month_total))
    print("Total: $" + str(GTotal))
    print(f"Average Change: ${round(sum(average)/len(average),2)}")
    print("Great Increase in Profits: ", greatest_increase_month, "($", g_increase, ")")
    print("Great Decrease in Profits: ", greatest_decrease_month, "($", g_decrease, ")")

# Write data to Financial_Analysis.txt
output_file = Path('Financial Analysis.txt')

with open(output_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Months: " + str(Month_total))
    file.write("\n")
    file.write("Total: $" + str(GTotal))
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average)/len(average),2)}")
    file.write("\n")
    file.write(f"Great Increase in Profits: {greatest_increase_month} $ {g_increase}")
    file.write("\n")
    file.write(f"Great Decrease in Profits: {greatest_decrease_month} $ {g_decrease}")