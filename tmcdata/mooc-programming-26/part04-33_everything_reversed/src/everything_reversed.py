# Write your solution here
def everything_reversed(x):
  ls = []
  for i in x:
    ls.append(i[::-1])

  return ls[::-1]