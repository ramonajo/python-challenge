import csv

budget_path = "PyBank/Resources/budget_data.csv"

#create empty lists for variables
months = []
total_profit = []
monthly_change = []

with open(budget_path) as text:
    budget = csv.reader(text)
    next(text)

    #count total months and total profit
    for row in budget:
        months.append(row[0])
        total_profit.append(int(row[1]))

    #changes in profit month to month
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])

    #find average
    average_change = round((sum(monthly_change)/len(months)),2)

    #find min and max
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    #find dates of min and max
    increase_date = months[monthly_change.index(greatest_increase)]
    decrease_date = months[monthly_change.index(greatest_decrease)]



print('Financial Analysis')
print(f'Total Months: {len(months)}')
print(f'Total Profit: ${sum(total_profit)}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase: {increase_date} {greatest_increase}')
print(f'Greatest Decrease: {decrease_date} {greatest_decrease}')

#output text file

output_path = "PyBank/Resources/budget_results.txt"
with open(output_path, 'w') as file:
    file.write('Financial Analysis\n')
    file.write(f'Total Months: {len(months)}')
    file.write(f'Total Profit: ${sum(total_profit)}\n')
    file.write(f'Average Change: ${average_change}\n')
    file.write(f'Greatest Increase: {increase_date} {greatest_increase}\n' )
    file.write(f'Greatest Decrease: {decrease_date} {greatest_decrease}\n')


