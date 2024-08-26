import csv

election_path = "PyPoll/Resources/election_data.csv"

#create empty lists for variables
total_votes = []
candidates = []
unique_candidate = []

votes_per_candidate = []
vote_percent = []

with open(election_path) as text:
    election = csv.reader(text)
    next(text)


    #counting total votes and candidates
    for row in election:
        total_votes.append(row[0])
        candidates.append(row[2])


    for candidate in set(candidates):
        #make unique candidates a list
        unique_candidate.append(candidate)

        #make votes per candiate a list
        votes = candidates.count(candidate)
        votes_per_candidate.append(votes)
        
        #percentage, making it a list
        percentage = (votes/369711)*100
        vote_percent.append(percentage)


    #finding the winner
    dict = {unique_candidate[i]: votes_per_candidate[i] for i in range(len(unique_candidate))}
    winner = max(dict, key = dict.get)
    

print('Election Results')
print(f'Total Votes: {len(total_votes)}')
for i in range(len(unique_candidate)):
    print(f'{unique_candidate[i]}: {round(vote_percent[i], 2)}% ({(str(votes_per_candidate[i]))} votes)')
print(f'Winner: {winner}')

#export as text file

output_path = "PyPoll/Resources/election_results.txt"
with open(output_path, 'w') as file:
    file.write('Election Results\n')
    file.write(f'Total Votes: {len(total_votes)}\n')
    for i in range(len(unique_candidate)):
       file.write(f'{unique_candidate[i]}: {round(vote_percent[i], 2)}% ({(str(votes_per_candidate[i]))} votes)\n')
    file.write(f'Winner: {winner}\n')