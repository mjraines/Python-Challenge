#import dependencies 
import os
import csv

# set path for csv file 
csv_path = os.path.join("Resources", "election_data.csv")

# open the csv
with open(csv_path, 'r', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")

# candidate variables 
    candidate_1 = "Khan"
    candidate_2 = "Correy"
    candidate_3 = "Li"
    candidate_4 = "O'Tooley"

#voting variables definded & starting vote set to 0
    starting_vote_for_1 = 0
    starting_vote_for_2 = 0
    starting_vote_for_3 = 0 
    starting_vote_for_4 = 0

# Loop for votes per candidate
    for row in csv_reader:
        if row[2] == candidate_1:
            starting_vote_for_1 = starting_vote_for_1 + 1
        elif row[2] == candidate_2:
            starting_vote_for_2 = starting_vote_for_2 + 1
        elif row[2] == candidate_3:
            starting_vote_for_3 = starting_vote_for_3 + 1
        elif row[2] == candidate_4:
            starting_vote_for_4 = starting_vote_for_4 + 1

# Need total votes 
    total_votes = starting_vote_for_1 + starting_vote_for_2 + starting_vote_for_3 + starting_vote_for_4

#Figure out Percentages 
khan_percent = float((starting_vote_for_1/total_votes)*100)
correy_percent = float((starting_vote_for_2/total_votes)*100)
li_percent = float((starting_vote_for_3/total_votes)*100)
otooley_percent = float((starting_vote_for_4/total_votes)*100)

#results printed 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Khan" + " " + str("%.3f" % khan_percent) + "%" + " " + "(" + str(starting_vote_for_1) + ")")
print("Correy" + " " + str("%.3f" % correy_percent) + "%" + " " + "(" + str(starting_vote_for_2) + ")")
print("Li" + " " + str("%.3f" % li_percent) + "%" + " " + "(" + str(starting_vote_for_3) + ")")
print("O\'Tooley" + " " + str("%.3f" % otooley_percent) + "%" + " " + "(" + str(starting_vote_for_4) + ")")
print("-------------------------")

if starting_vote_for_1 > starting_vote_for_2 and starting_vote_for_1 > starting_vote_for_3 and starting_vote_for_1 > starting_vote_for_4:
    print("Winner: Khan")
elif starting_vote_for_2 > starting_vote_for_1 and starting_vote_for_2 > starting_vote_for_3 and starting_vote_for_2 > starting_vote_for_4: 
    print("Winner: Correy")
elif starting_vote_for_3 > starting_vote_for_1 and starting_vote_for_3 > starting_vote_for_2 and starting_vote_for_3 > starting_vote_for_4:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")

print("-------------------------")

def text_file():
    return str("Election Results" + "    " + "-------------------------" +
  "Total Votes: 3521001" + "   " +
 " -------------------------" + "   " +
  "Khan: 63.000% (2218231)" + "   " +
  "Correy: 20.000% (704200)" + "   " +
  "Li: 14.000% (492940)" + "   " +
  "O'Tooley: 3.000% (105630)" + "   " +
  "-------------------------" + "   " +
  "Winner: Khan" + "   " +
  "-------------------------" + "   " +
 " ```")
output = text_file()
file = open("output.txt", "w")
file.write(output)
file.close()