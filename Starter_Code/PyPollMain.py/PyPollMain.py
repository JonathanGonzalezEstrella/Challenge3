import os
import csv

# Path to the CSV file
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
# Initialize variables
total_votes = 0
candidates_votes = {}

# Open and read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Increment total_votes
        total_votes += 1
        
        # If the candidate is in the dictionary, increment their vote count
        # Otherwise, add the candidate to the dictionary with a vote count of 1
        candidate_name = row[2]  # Assuming candidate name is in the third column
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
        else:
            candidates_votes[candidate_name] = 1

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
winner = max(candidates_votes, key=candidates_votes.get)
print(f"Winner: {winner}")
print("-------------------------")
