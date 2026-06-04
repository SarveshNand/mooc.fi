# Write your solution here
def all_the_longest(strings):
  max_len = 0
  result = []

  for word in strings:
    if len(word) > max_len:
      max_len = len(word)

  for word in strings:
    if len(word) == max_len:
      result.append(word)

  return result