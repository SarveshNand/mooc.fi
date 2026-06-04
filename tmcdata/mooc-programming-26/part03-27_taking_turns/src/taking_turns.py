# Write your solution here
limit = int(input("Please type in a number: "))
left = 1
right = limit

while left <= right:
  if left == right:
    print(left)
    break

  print(left)
  left += 1

  print(right)
  right -= 1