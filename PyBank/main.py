import os
import csv

budget_file = os.path.join("Resources", "budget_data.csv")

total_months = 0
net_total = 0
list_profit_loss = []
greatest = 0
smallest = 0
previous_value = None  

with open(budget_file) as file:
    csv_reader = csv.reader(file, delimiter=",")

    csv_header = next(csv_reader)
    

    for row in csv_reader:
        # print(row)
        total_months += 1
        value_in_column = int(row[1])
        net_total += value_in_column

        list_profit_loss.append(value_in_column)

        if previous_value is not None:
            change = value_in_column - previous_value
            if change > greatest:
                greatest = change
                g_month = row[0]
                

        if previous_value is not None:
            small_change = value_in_column - previous_value
            if small_change < smallest:
                smallest = small_change
                s_month = row [0]

                
        previous_value = value_in_column


print("                           ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change : ${round((list_profit_loss[len(list_profit_loss) - 1] - (list_profit_loss[0])) / (len(list_profit_loss)-1),2)}")
print(f"Greatest Increase in Profits: {g_month} (${greatest})")
print(f"Greatest Decrease in Profits: {s_month} (${smallest})")