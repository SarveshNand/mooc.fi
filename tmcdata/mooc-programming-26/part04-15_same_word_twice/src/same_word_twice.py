# Write your solution here
count = 0
words = []
while True:
  word = input("Word: ")
  if word not in words:
    words.append(word)
    count += 1
  else:
    break

print(f"You typed in {count} different words")