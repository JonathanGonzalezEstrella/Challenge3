# Financial Analysis Script

## Overview
This Python script is designed to analyze financial records for a company using data from a CSV file. The script calculates the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, the average change in "Profit/Losses" between months over the entire period, the greatest increase in profits (date and amount) over the entire period, and the greatest decrease in losses (date and amount) over the entire period.

## Requirements
- Python 3.x
- CSV file containing financial data (`budget_data.csv`)

## CSV File Format
The CSV file should have the following columns:
- `Date` (in the format `Jan-2010`)
- `Profit/Losses` (integer value)

Example:
Date,Profit/Losses
Jan-2010,867884
Feb-2010,984655

## How to Run the Script
1. Ensure that Python 3 is installed on your machine.
2. Place the `budget_data.csv` file in the following directory relative to the script: `../PyBank/Resources/`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script by typing `python <script_name>.py` and hit Enter. 

## Output
The script will output the following financial analysis to the console:
- Total Months: The total number of months included in the dataset.
- Total: The net total amount of "Profit/Losses" over the entire period.
- Average Change: The average change in "Profit/Losses" between months over the entire period.
- Greatest Increase in Profits: The date and amount of the greatest increase in profits.
- Greatest Decrease in Profits: The date and amount of the greatest decrease in losses.

## Example Output
Financial Analysis
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)