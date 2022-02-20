import csv
import os


file_to_load = os.path.join('Resources/election_results2.csv')
with open(file_to_load) as election_data:
    print(election_data) 

#file  name variable to direct path to file we are writing out to
file_to_save = os.path.join("analysis", "election_analysis2.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Hello again Mickey\n")
#     txt_file.write("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~**~*~*~*~**~\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

candidate_options = set()
candidate_options2 = {}
total_votes = 0
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:

#read and analyze data here

#read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print header row in the CSV file.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        
        #this will tell it to look for the candidate name in the dictionary       
        if candidate_name not in candidate_votes: 
            #program will assign the key of "candidate name" to value 1 in candidate_votes
            candidate_votes[candidate_name] = 1
        else: 
            candidate_votes[candidate_name] += 1


        #this if statement is needed if you have defined candidate_options as a list. We have defined it as a set.
        #if candidate_name not in candidate_options:
        
        #this is a set; it will not add things to the list again automatically, no if statement needed
        candidate_options.add(candidate_name) #this addds to the set
        candidate_options2[candidate_name] = True #this is a boolean funciton on a dictionary you defined



    # Better way to do this (Pratik)
    # candidate_votes = {}
    # for row in file_reader:
    #     total_votes += 1
    #     candidate_name = row[2]
    #     candidate_votes[candidate_name] += 1
    # candidate_votes.keys()
    
print(total_votes)
# print(candidate_options) #from set
# print(candidate_options2) #from dictionary
# print(candidate_options2.keys()) #from dictionary, candidates (keys) only
print(candidate_votes)

