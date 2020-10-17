import csv 

with open("PyBank\Resources\Budget_data.csv", "r") as file:
    budget = csv.reader(file)
    next(budget) 

# create empty lists for each column of the csv 
    month = []
    profit = []

    #;opulate  lists
    for row in budget: 
        month.append(row[0])
        profit.append(row[1])

# print(profit)

# set up variables for camparison 
max_profit = 0 
min_profit = 0 
sprofit = 0 
total = float(profit[0])

for p in range (1,len(month)):
    x = float(profit[p-1])
    y = float(profit[p])

    dprofit = float(y - x)
    sprofit = sprofit + dprofit
    total = total + y

# find max profit and loss
    if dprofit > max_profit:
        max_profit = dprofit
        high_month = month[p]

    elif dprofit < float(min_profit):
        min_profit = dprofit
        low_month = month[p]

# find average 
avprofit = round((sprofit/(len(month)-1)),2)
min_profit = round(min_profit)
max_profit = round(max_profit)
total = round(total)

# write results to a text file 
results = open("PyBank\Analysis\Budget_Results.txt", "w")

results.write("Financial Analysis \n----------------------------")
results.write("\nTotal Months: "+ str(len(month)))
results.write("\nTotal: $" + str(total))
results.write("\nAverage  Change: $" +str(avprofit))
results.write("\nGreatest Increase in Profits: " +high_month+ " ($" +str(max_profit)+ ")")
results.write("\nGreatest Decrease in Profits: " +low_month+ " ($" +str(min_profit)+ ")")

results.close()
