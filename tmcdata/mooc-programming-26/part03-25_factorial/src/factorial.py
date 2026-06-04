# Write your solution here
while True:
  user_input = int(input("Please type in a number: "))

  if user_input <= 0:
    print("Thanks and bye!")
    break

  factorial = 1
  for i in range(1, user_input + 1):
    factorial *= i
  
  print(f"The factorial of the number {user_input} is {factorial}")