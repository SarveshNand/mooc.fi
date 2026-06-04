# Write your solution here
items = int(input("How many items: "))
my_list = []
for i in range(1, items+1):
  value = int(input(f"Item {i}: "))
  my_list.append(value)

print(my_list)