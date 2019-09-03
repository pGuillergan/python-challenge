import os
import csv
import math

csv_path = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_profit_loss = 0
total_change = 0
current_change = 0
average_change = 0
last_value = 0
skip_first_item = True
great_increase = []
great_decrease = []

with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    #print(header)

    for row in csv_reader:
        total_months += 1
        total_profit_loss += int(row[1])
        
        current_change = int(row[1]) - last_value
        total_change += current_change
        
        #skip the first item
        if skip_first_item:
            total_change = 0
            great_increase = row
            great_decrease = row
            skip_first_item = False

        #find the greatest increase and decrease
        if  current_change >= int(great_increase[1]) :
            great_increase = [row[0], current_change]

        if current_change <= int(great_decrease[1]):
            great_decrease = [row[0], current_change]

        last_value = int(row[1])

    average_change = round( total_change / (total_months-1), 2)
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_increase[0]} {great_increase[1]}")
print(f"Greatest Decrease in Profits: {great_decrease[0]} {great_decrease[1]}")
print("----------------------------")

txt_path = os.path.join('Resources', 'PyBank_output.txt')

with open(txt_path, 'w') as txt_file:
    txt_file.write("---------------------------- \n")
    txt_file.write("Financial Analysis \n")
    txt_file.write("---------------------------- \n")
    txt_file.write(f"Total Months: {total_months} \n")
    txt_file.write(f"Total: ${total_profit_loss} \n")
    txt_file.write(f"Average Change: ${average_change} \n")
    txt_file.write(f"Greatest Increase in Profits: {great_increase[0]} {great_increase[1]} \n")
    txt_file.write(f"Greatest Decrease in Profits: {great_decrease[0]} {great_decrease[1]} \n")
    txt_file.write("---------------------------- \n")
