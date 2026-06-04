# Write your solution here
limit = int(input("Please type in a number: "))
for i in range(1, limit + 1, 2):
  if i + 1 <= limit:
    print(i + 1)
    print(i)
  else:
    print(i)