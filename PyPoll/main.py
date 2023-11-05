import os
import csv

total_votes = 0
candidates_names = []
candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0

election_file = os.path.join("PyPoll/Resources/election_data.csv")

with open(election_file) as file:
    csv_reader = csv.reader(file, delimiter = ",")

    csv_header = next(csv_reader)
    
    for row in (csv_reader):
        # print(row)
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates_names:
            candidates_names.append(candidate)
        winner = None
        if candidate == candidates_names[0]:
            candidate_1_votes += 1
        elif candidate == candidates_names[1]:
            candidate_2_votes += 1
        elif candidate == candidates_names[2]:
            candidate_3_votes += 1   
            if candidate_1_votes > candidate_2_votes and candidate_3_votes:
                winner = candidates_names[0]
            elif candidate_2_votes > candidate_1_votes and candidate_3_votes:
                winner = candidates_names[1]
            elif candidate_3_votes > candidate_1_votes and candidate_2_votes:
                winner = candidates_names[2]
            
percentage1 = (round(float(candidate_1_votes / total_votes *100),3)) 
percentage2 = (round(float(candidate_2_votes / total_votes * 100),3))
percentage3 = (round(float(candidate_3_votes / total_votes * 100),3))

print("                       ")
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"{candidates_names[0]} {percentage1}% ({candidate_1_votes})")
print(f"{candidates_names[1]} {percentage2}% ({candidate_2_votes})")
print(f"{candidates_names[2]} {percentage3}% ({candidate_3_votes})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")
