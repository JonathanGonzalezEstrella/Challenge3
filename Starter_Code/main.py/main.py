import os
import csv

# Path to the CSV file (using a string for the Windows file path)
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
total_profit_losses = 0
prev_month_profit_losses = 0
profit_losses_change = []
months = []

# Open and read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        
        # Sum the total amount of "Profit/Losses"
        total_profit_losses += int(row[1])
        
        # Calculate changes in "Profit/Losses", excluding the first month
        if total_months > 1:
            change = int(row[1]) - prev_month_profit_losses
            profit_losses_change.append(change)
            months.append(row[0])
        
        prev_month_profit_losses = int(row[1])

# Calculate the average of the changes in "Profit/Losses"
average_change = sum(profit_losses_change) / len(profit_losses_change)

# Determine the greatest increase and decrease in profits
greatest_increase = max(profit_losses_change)
greatest_decrease = min(profit_losses_change)
greatest_increase_month = months[profit_losses_change.index(greatest_increase)]
greatest_decrease_month = months[profit_losses_change.index(greatest_decrease)]

# Print the analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
