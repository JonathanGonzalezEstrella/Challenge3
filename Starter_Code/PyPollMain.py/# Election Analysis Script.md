# Election Analysis Script

## Overview
This Python script automates the vote-counting process for an election. It reads from a CSV file containing election data and calculates the total number of votes cast, lists all candidates who received votes, calculates the percentage of votes each candidate won, the total number of votes each candidate won, and determines the winner of the election based on the popular vote.

## Requirements
- Python 3.x
- CSV file containing election data (`election_data.csv`)

## CSV File Format
The CSV file should have the following columns:
- `Voter ID` (unique identifier for each vote)
- `County` (the county where the vote was cast)
- `Candidate` (the name of the candidate the vote was cast for)

Example:
Voter ID,County,Candidate
102294,Marsh,Khan
102295,Marsh,Correy


## How to Run the Script
1. Ensure that Python 3 is installed on your machine.
2. Place the `election_data.csv` file in the following directory relative to the script: `../PyPoll/Resources/`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script by typing `python <script_name>.py` and hit Enter.

## Output
The script outputs the analysis of the election to the console, which includes:
- Total Votes: The total number of votes cast in the election.
- For each candidate:
  - The percentage of votes they won.
  - The total number of votes they won.
- Winner: The name of the candidate who won the election based on the popular vote.

## Example Output
Election Results
Total Votes: 3521001
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
Winner: Khan