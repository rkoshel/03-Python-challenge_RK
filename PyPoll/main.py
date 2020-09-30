# Set modules
import os
import csv
from pathlib import Path 

# Path to collect data from the Resources folder
votecsv = os.path.join('..', 'Resources', 'election_data.csv')

# Set Variables
votes_list = 0
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(votecsv, newline = "", encoding = "utf-8") as votereader:
    
    csvreader = csv.reader(votereader, delimiter = ",")
    #with open(votecsv, 'r') as votereader:

    #votecsv = csv.reader(votereader, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:

        total_votes +=1

        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Combine rating with name
candidates = ["Khan" , "Correy" , "Li" , "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
roster = dict(zip(candidates, votes))
key = max(roster, key=roster.get)

# Print Statements
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print("------------------------")
print(f"Winner: {key}")
print("------------------------")

# Write data to Vote.txt
output_file = Path('Vote.txt')

with open(output_file, "w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write("------------------------")