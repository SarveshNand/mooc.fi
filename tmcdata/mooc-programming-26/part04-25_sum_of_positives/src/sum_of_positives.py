# Write your solution here
def sum_of_positives(x):
  summed = 0
  for i in x:
    if i > 0:
      summed += i
  
  return summed