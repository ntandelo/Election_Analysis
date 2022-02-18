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

#initialize total votes counter, which means set it to zero
total_votes = 0

candidate_options = []
# Open the election results and read the file.

#new dictionary to get votes tied to candidates
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    #print(headers)
 
    # This is a for loop. It says, "for a new variable 'row', in the file_reader,
    # count up total_votes in increments of 1
    for row in file_reader:
        total_votes = total_votes + 1
        #print candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...once you add it to the string stop adding
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes/float(total_votes)*100)
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    # Print the candidate list.
    print(candidate_votes)

    #print(total_votes)

