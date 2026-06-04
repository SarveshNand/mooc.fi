# Write your solution here
def squared(text, size):
  index = 0
  for row in range(size):
    for col in range(size):
      print(text[index], end="")
      index = (index + 1) % len(text)
    print()

if __name__ == "__main__":
  squared("ab", 3)
  print()
  squared("aybabtu", 5)