import csv
from collections import Counter

#File to open
file_to_open = "Resources/election_data.csv"

# Read csv and convert to dictionaries
with open(file_to_open) as election_data:
    reader = csv.reader(election_data)
    
    # Next to skip title row in csv
    next(reader)
    voter_ID = []
    county = []
    candidates = []
    voter_total = 0
    set_of_candidate = set()
    
# The total number of votes cast
    for row in reader:
        voter_ID.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
        voter_total = voter_total + 1
        
        # A complete list of candidates who received votes
        set_of_candidate.add(row[2])

# The total number of votes each candidate won
    list_of_candidates = list(set_of_candidate)

    z = Counter(candidates).items()
    
    #convert counter printout to list
    candidate = list(z)

    #Create a list for each candidate
    Kahn = candidate[0]
    Correy = candidate[1]
    Li = candidate[2]
    O_Tooley = candidate[3]

    Kahn_list = list(Kahn)
    Correy_list = list(Correy)
    Li_list = list(Li)
    O_Tooley_list = list(O_Tooley)

    #seperate votes out from candidate name
    Kahn_votes = Kahn_list[1]
    Correy_votes = Correy_list[1]
    Li_votes = Li_list[1]
    O_Tooley_votes = O_Tooley_list[1]

    # The percentage of votes each candidate won
    Kahn_count = (Kahn_votes/voter_total)
    Kahn_perc = format(Kahn_count, ".3%")

    Correy_count = (Correy_votes/voter_total)
    Correy_perc = format(Correy_count, ".3%")

    Li_count = (Li_votes/voter_total)
    Li_perc = format(Li_count, ".3%")

    O_Tooley_count = (O_Tooley_votes/voter_total)
    O_Tooley_perc = format(O_Tooley_count, ".3%")

    #variable set up for easier f string creation for text file and print.
    kahn_write = (f"Khan: {Kahn_perc} ({Kahn_votes})")
    correy_write = (f"Correy: {Correy_perc} ({Correy_votes})")
    li_write = (f"Li: {Li_perc} ({Li_votes})")
    o_tooley_write = (f"O'Tooley: {O_Tooley_perc} ({O_Tooley_votes})") 

    results = (f"Election Results \n----------------------\nTotal Votes: {voter_total}\n----------------------\n{kahn_write}\n{correy_write}\n{li_write}\n{o_tooley_write}\n----------------------\nWinner : Kahn\n----------------------")

#print results
print(results)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
election_results = open("election_results.txt", "w")
election_results.write(results)
election_results.close()