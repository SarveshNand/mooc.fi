# Write your solution here
ls = []
while True:
  user = int(input("New item: "))
  if user != 0:
    ls.append(user)
    print(f"The list now: {ls}")
    print(f"The list in order: {sorted(ls)}")
  else:
    print("Bye!")
    break