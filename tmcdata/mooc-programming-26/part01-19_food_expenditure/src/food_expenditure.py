# Write your solution here
week_eat = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
spent_money = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {(week_eat * price + spent_money) / 7} euros")
print(f"Weekly: {week_eat * price + spent_money} euros")