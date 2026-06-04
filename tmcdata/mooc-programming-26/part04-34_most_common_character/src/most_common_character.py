# Write your solution here
def most_common_character(text):
  counts = {}

  for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
  
  most_common = text[0]

  for ch in text:
    if counts[ch] > counts[most_common]:
      most_common = ch

  return most_common