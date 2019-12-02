#import the data set
import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

#total number of months included in the dataset, total count of the rows in column1
    data = [l for l in csvreader]
    row_count = len(data)
    print (row_count)

#A complete list of candidates who received votes
voters = []
# loop all the rows, and extract the  column
for i in range(len(data)-1):
    votername=data[i][2]
    #print(votername)
    #add each results into the average list
    voters.append(votername)

#use set to extract the unique value of the list
unique_voters = set(voters)
#count the unique value of the list
unique_voters_count = len(unique_voters)
print(unique_voters)

#count the occurance of each item in the list
vote_li = voters.count('Li')
vote_Khan = voters.count('Khan')
vote_Correy = voters.count('Correy')
vote_OTooley = voters.count("O'Tooley")

#count the percentage of the each item's occurance

Li_percentage = (vote_li/row_count)
print(f"{Li_percentage:.0%}")
Khan_percentage = (vote_Khan/row_count)
print(f"{Khan_percentage:.0%}")
Correy_percentage = (vote_Correy/row_count)
print(f"{Correy_percentage:.0%}")
OTooley_percentage = (vote_OTooley/row_count)
print(f"{OTooley_percentage:.0%}")


# make a dictionary of the two lists, and zip the name with the votes
candidates = ["Li", "Khan", "Correy","O'Tooley"]
vote = [vote_li, vote_Khan,vote_Correy,vote_OTooley]
dict_winner = dict(zip(candidates,vote))
print(dict_winner)

# using a max function of the dictionary to get the winner 
winner = max(dict_winner, key=dict_winner.get)
print(winner)

# print results
Results = (   
f"Election Results \n"
f"---------------------- \n"
f"Total votes: {row_count} \n"
f"---------------------- \n"
f"Khan: {Khan_percentage:.0%} ({vote_Khan}) \n"
f"Correy: {Correy_percentage:.0%} ({vote_Correy}) \n"
f"Li: {Li_percentage:.0%} ({vote_li}) \n"
f"O'Tooley: {OTooley_percentage:.0%} ({vote_li}) \n"
f"------------------------------ \n"
f"Winner: {winner} \n"
f"------------------------------ \n"
)
print(Results)

#write a text file to export the results
output = os.path.join('Resources/Poll_Analysis.txt')
with open(output, 'w') as file:
    txtwriter = file.write(Results)
