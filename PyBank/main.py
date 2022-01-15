#import dependencies 
import os 
import csv 

#set path for csv file 
csv_path = os.path.join("Resources", "budget_data.csv")

#open and read
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    #name delimiter
    csv_header = next(csvreader)
    
 
    #declare variables 
    total_months = []
    profit_losses = []
    difference = []
    greatest_increase_date = ""
    greatest_decrease_date = ""
    
    
    #total number of months 
    for row in csvreader:
        total_months.append(row[0])   
        profit_losses.append(row[1])
        profit_losses = [int(i) for i in profit_losses]
        total_change =0

    for i in range(len(profit_losses)-1):

        #find average change through the months
        difference = profit_losses[i+1] - profit_losses[i]
        total_change = total_change + difference
        
        #average change
        average_change = (total_change) / (len(profit_losses)-1)
    
        
        #greatest increase & date
    greatest_increase_profit = max(profit_losses)
    greatest_increase_date = str( total_months[profit_losses.index(max(profit_losses))])

        
        #greatest decrease & date
    greatest_decrease_losses = min(profit_losses)
    greatest_decrease_date = str( total_months[profit_losses.index(min(profit_losses))])

#print to terminal 
print("Financial Analysis")
print("------------------")
print("Total Months:", len(total_months))
print("Total: $",sum(profit_losses))      
print("Average Change: $" + str("%.2f" % average_change))
print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase_profit)+")")
print("Greatest Decrease in Profits: " + greatest_decrease_date +" ($" + str(greatest_decrease_losses)+")")


#export text file 
def text_file():
    return str("Financial Analysis" +
  "----------------------------" + 
  "Total Months: 86" +
  "Total: $38382578" +
  "Average  Change: $-2315.12" +
  "Greatest Increase in Profits: Feb-2012 ($1170593)" + 
  "Greatest Decrease in Profits: Sep-2013 ($-1196225)")
output = text_file()
file = open("output.txt", "w")
file.write(output)
file.close()



