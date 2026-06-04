# Write your solution here
def distinct_numbers(x):
  ls = []
  for i in x:
    if i not in ls:
      ls.append(i)
  return sorted(ls)