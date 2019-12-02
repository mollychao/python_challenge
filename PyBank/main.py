#import the data set
import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

#total number of months included in the dataset, total count of the rows in column1
    data = [l for l in csvreader]
    row_count = len(data)
    print (row_count)
    
    
total=0
#total amount of profile/losses
        
for row in data:
    total+=int(row[1])
print(total)


#create the list to host the difference of the rows
average=[]
# loop all the rows, and extract the second column
for i in range(len(data)-1):
    current=data[i][1]
    next=data[i+1][1]
    #calculate the difference between two sequential rows
    difference=int(next)-int(current)
    #add each results into the average list
    average.append(difference)

#calculate the average of the list
average_change=sum(average)/len(average)
print(average_change)

#calculate the max and min profit 
max_value = max(average)
print(max_value)
min_value = min(average)
print(min_value)

#print results
Results = (
f"Financial Analysis \n"
f"---------------------- \n"
f"Total Months: {row_count} \n"
f"Total Revenue: ${total} \n"
f"Average Revenue Change: ${average_change} \n"
f"Greatest Increase in Revenue: ${max_value} \n"
f"Greatest Decrease in Revenue: ${min_value} \n")
print(Results)

#write a text file to export the results
output = os.path.join('Resources/Financial_Analysis.txt')
with open(output, 'w') as file:
    txtwriter = file.write(Results)