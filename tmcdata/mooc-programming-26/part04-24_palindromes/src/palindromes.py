# Write your solution here
def palindromes(s):
  return s == s[::-1]

while True:
  word = input("Please type in a palindrome: ")

  if palindromes(word):
    print(f"{word} is a palindrome!")
    break
  else:
    print("that wasn't a palindrome")
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!