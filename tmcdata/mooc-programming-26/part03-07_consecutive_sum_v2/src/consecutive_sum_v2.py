# Write your solution here
limit = int(input("Limit: "))
summ = 0
num = 1
calculation = ""
while summ < limit:
  summ += num

  if num > 1:
    calculation += " + "
  
  calculation += str(num)
  num += 1
print(f"The consecutive sum: {calculation} = {summ}")