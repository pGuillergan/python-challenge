import os
import csv
import math
import operator

csv_path = os.path.join("Resources", "election_data.csv")

total_votes_cast = 0
# unique key is full name
votes_per_candidates = {}
winner = ""

with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #skip the header
    next(csv_reader)

    for row in csv_reader:
        total_votes_cast += 1
        if row[2] in votes_per_candidates.keys():
            votes_per_candidates[row[2]] += 1
        else:
            votes_per_candidates[row[2]] =  0

    print("-------------------------")
    print("Election Results!!!")
    print("-------------------------")
    print(f"Total Votes: {total_votes_cast}")
    print("-------------------------")
    for key in votes_per_candidates:
        percentage = (votes_per_candidates[key] / total_votes_cast)  * 100
        print(f"{key}: {percentage: .3f}% ({votes_per_candidates[key]})")
    print("-------------------------")
    winner = max(votes_per_candidates.items(), key=operator.itemgetter(1))[0]
    print(f"Winner: {winner}")
    print("-------------------------")

#print out text file
txt_path = os.path.join('Resources', 'PyPoll_output.txt')
with open(txt_path, 'w') as txt_file:
    txt_file.write("------------------------- \n")
    txt_file.write("Election Results!!! \n")
    txt_file.write("------------------------- \n")
    txt_file.write(f"Total Votes: {total_votes_cast} \n")
    txt_file.write("------------------------- \n")
    for key in votes_per_candidates:
        percentage = (votes_per_candidates[key] / total_votes_cast)  * 100
        txt_file.write(f"{key}: {percentage: .3f}% ({votes_per_candidates[key]}) \n")
    txt_file.write("------------------------- \n")
    #winner = max(votes_per_candidates.items(), key=operator.itemgetter(1))[0]
    txt_file.write(f"Winner: {winner} \n")
    txt_file.write("------------------------- \n")