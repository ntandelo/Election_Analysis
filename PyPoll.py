#The data we need to retrieve


# the total number of votes cast
# Complete list of candidates who got votes
# percentage of votes each candidate won
# the total number of votes each candidate won
# winner of election 

#file is Resources/election_results.csv
# import csv
# dir(csv)
# print(dir(csv))

#these are dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    print(headers2)