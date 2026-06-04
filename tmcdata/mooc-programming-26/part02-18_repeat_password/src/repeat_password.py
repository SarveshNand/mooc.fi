# Write your solution here
psswd = input("Password: ")
while True:
  rep_psswd = input("Repeat password: ")
  if rep_psswd == psswd:
    print("User account created!")
    break
  
  print("They do not match!")