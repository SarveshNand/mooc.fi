# Write your solution here
def shortest(strings):
  shortest_word = strings[0]

  for word in strings:
    if len(word) < len(shortest_word):
      shortest_word = word

  return shortest_word