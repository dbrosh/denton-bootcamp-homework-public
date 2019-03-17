import csv

# Files to load
file_to_load = "resources/budget_data.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # use of next to skip title row in csv file
    next(reader) 
    revenue = []
    month = []
    rev_change = []

    # sum of months
    for row in reader:

        revenue.append(float(row[1]))
        month.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(month))
    print("Total Revenue: $", sum(revenue))


    # total of difference between revenue, found total revnue change and found out max revenue change and min revenue change 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_month = str(month[rev_change.index(max(rev_change))])
        min_rev_change_month = str(month[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_month,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_month,"($", min_rev_change,")")
