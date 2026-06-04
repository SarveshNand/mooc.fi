# Write your solution here
def even_numbers(x):
  ls = []
  for i in x:
    if i % 2 == 0:
      ls.append(i)
  
  return ls