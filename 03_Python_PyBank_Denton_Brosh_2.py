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

    # total of difference between revenue, found total revnue change and found out max revenue change and min revenue change 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_month = str(month[rev_change.index(max(rev_change))])
        min_rev_change_month = str(month[rev_change.index(min(rev_change))])

    # create a srting to print and for txt file
    months = len(month)
    total_months = (f"Total Months: {months}")
    tr = sum(revenue)
    total_revenue = (f"Total Revenue: ${tr}")
    avgch = round(avg_rev_change)
    average_change = (f"Average Revenue Change: ${avgch}")
    greatest_increase_rev = (f"Greatest Increase in Revenue: {max_rev_change_month} (${max_rev_change})")
    greatest_decrease_rev = (f"Greatest Decrease in Revenue: {min_rev_change_month} (${min_rev_change})")
    results = (f"Financial Analysis \n-------------------------------- \n{total_months} \n{total_revenue} \n{average_change} \n{greatest_increase_rev} \n{greatest_decrease_rev}")
    
#print results and create txt file
print(results)

financial_analysis = open("financial_analysis.txt", "w")
financial_analysis.write(results)
financial_analysis.close()