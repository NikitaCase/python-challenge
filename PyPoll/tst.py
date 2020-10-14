import csv
import os

vote_count = 0 
Khan = 0
Correy = 0
Li = 0 
OTooley = 0 
fifth = 0 


with open("PyPoll\Resources\election_data.csv", "r") as file:
    votes = csv.reader(file)
    for wote in votes:
        print(wote)
        break

'''
with open(source) as csv_file:
    election_data = csv.reader(csv_file, delimeter = ",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
'''
    