# Write your solution here
ls = []
while True:
  print(f"The list is now {ls}")
  opt = input("a(d)d, (r)emove or e(x)it: ")

  if opt == "d":
    ls.append(len(ls) + 1)
  elif opt == "r":
    if len(ls) > 0:
      ls.pop()
  elif opt == "x":
    print("Bye!")
    break