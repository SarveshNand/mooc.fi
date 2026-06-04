# Write your solution here
def length_of_longest(strings):
  longest = 0

  for word in strings:
    if len(word) > longest:
      longest = len(word)

  return longest