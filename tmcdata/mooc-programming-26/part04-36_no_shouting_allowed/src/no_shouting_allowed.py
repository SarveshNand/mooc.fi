# Write your solution here
def no_shouting(strings):
  ls = []
  for word in strings:
    if not word.isupper():
      ls.append(word)

  return ls