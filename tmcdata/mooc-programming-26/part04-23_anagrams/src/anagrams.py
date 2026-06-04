# Write your solution here
def anagrams(x, y):
  stuff1 = ""
  stuff2 = ""
  for i in x:
    stuff1 += i
  for i in y:
    stuff2 += i

  if sorted(stuff1) == sorted(stuff2):
    return True
  else:
    return False

if __name__ == "__main__":
  print(anagrams("tame", "meta"))