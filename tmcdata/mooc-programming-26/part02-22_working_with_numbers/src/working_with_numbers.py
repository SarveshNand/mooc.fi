# Write your solution here
count = 0
summ = 0
pos_num = 0
neg_num = 0
while True:
  print("Please type in integer numbers. Type in 0 to finish.")
  num = int(input("Number: "))
  if num == 0:
    break

  if num > 0:
    pos_num += 1
  else:
    neg_num += 1

  count += 1
  summ += num

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {summ}")
print(f"The mean of the numbers is {summ / count}")
print(f"Positive numbers {pos_num}")
print(f"Negative numbers {neg_num}")