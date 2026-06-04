# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index < len(word):
  if word[index] == character and index + 3 <= len(word):
    print(word[index:index+3])

  index += 1