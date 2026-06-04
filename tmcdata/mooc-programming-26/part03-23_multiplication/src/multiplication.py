# Write your solution here
user = int(input("Please type in a number: "))
for i in range(1, user + 1):
  for j in range(1, user + 1):
    result = i * j
    print(f"{i} x {j} = {result}")