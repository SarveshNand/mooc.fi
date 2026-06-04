# Write your solution here
def no_vowels(alphabets):
  words = ""

  for word in alphabets:
    if word not in "aeiou":
      words += word
  
  return words