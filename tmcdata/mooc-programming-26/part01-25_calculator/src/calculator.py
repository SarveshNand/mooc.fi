# Write your solution here
x = int(input("Number 1: "))
y = int(input("Number 2: "))
add = x + y
subtract = x - y
multiply = x * y
operation = input("Operation: ")
if operation == "add":
  print(f"{x} + {y} = {add}")
elif operation == "subtract":
  print(f"{x} - {y} = {subtract}")
elif operation == "multiply":
  print(f"{x} * {y} = {multiply}")