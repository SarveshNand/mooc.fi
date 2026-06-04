# Write your solution here
def longest_series_of_neighbours(numbers):
  if not numbers:
    return 0

  longest = 1
  current = 1

  for i in range(1, len(numbers)):
    if abs(numbers[i] - numbers[i - 1]) == 1:
      current += 1
    else:
      current = 1

    if current > longest:
      longest = current

  return longest