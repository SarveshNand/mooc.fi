# Write your solution here
def longest(strings: list):
  ls = strings[0]

  for string in strings:
    if len(string) > len(ls):
      ls = string
  
  return ls
