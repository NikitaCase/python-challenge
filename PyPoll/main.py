import csv

vote_count = 0 
Khan = 0
Correy = 0
Li = 0 
OTooley = 0 
fifth = 0 


with open("PyPoll\Resources\election_data.csv", "r") as file:
    votes = csv.reader(file)
    next(votes)

    for vote in votes:
        vote_count = vote_count + 1

        if vote[2] == 'Khan':
            Khan += 1
        elif vote[2] == 'Correy':
            Correy = Correy + 1
        elif vote[2] == "Li":
            Li += 1
        elif vote[2] == "O'Tooley":
            OTooley = OTooley + 1
        else:
            fifth = fifth + 1 

KhanP = round(((Khan/vote_count)*100),3)
CorreyP = round(((Correy/vote_count)*100),3)
LiP = round(((Li/vote_count)*100),6)
OTooleyP = round(((OTooley/vote_count)*100),3)
if fifth >0:
    fifthP = round(((fifth/vote_count)*100),3)
else:
    fifthP = 0

if Khan > Correy and Khan > Li and Khan > OTooley:
    winner= 'Khan'
elif Correy > Khan and Corey > Li and Correy > OTooley:
    winner = 'Correy'
elif Li > Khan and Li > Correy and Li > Otooley:
    winner = 'Li'
else:
    winner = "O'Tooley"



results = open("PyPoll\Analysis\election_results.txt", "w")

results.write("Election Results\n-------------------------\nTotal Votes: " +str(vote_count))
results.write("\n-------------------------")
results.write("\nKhan: "+str(KhanP)+"% ("+str(Khan)+")")
results.write("\nCorrey: " +str(CorreyP)+"% ("+str(Correy)+")")
results.write("\nLi: " +str(LiP)+"% ("+str(Li)+")")
results.write("\nO'Toole: " +str(OTooleyP)+"% ("+str(OTooley)+")")
results.write("\n-------------------------")
results.write("\nWinner: " +winner+ "\n-------------------------")

results.close()

