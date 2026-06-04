# Write your solution here
while True:
  user = input("Editor: ").lower()
  if user == "visual studio code":
    print("an excellent choice!")
    break

  elif user == "word" or user == "notepad":
    print("awful")

  else:
    print("not good")