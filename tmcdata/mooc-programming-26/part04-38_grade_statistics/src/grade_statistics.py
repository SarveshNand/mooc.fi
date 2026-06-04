# Write your solution here
all_points = []
grades = [0, 0, 0, 0, 0, 0]

while True:
  line = input("Exam points and exercises completed: ")

  if line == "":
    break

  parts = line.split()
  exam = int(parts[0])
  exercises = int(parts[1])

  exercise_points = exercises // 10
  total_points = exam + exercise_points

  # determine grade
  if exam < 10:
    grade = 0
  elif total_points <= 14:
    grade = 0
  elif total_points <= 17:
    grade = 1
  elif total_points <= 20:
    grade = 2
  elif total_points <= 23:
    grade = 3
  elif total_points <= 27:
    grade = 4
  else:
    grade = 5

  all_points.append(total_points)
  grades[grade] += 1

print("Statistics:")

# average
average = sum(all_points) / len(all_points)
print(f"Points average: {average:.1f}")

# pass percentage (grades 1–5)
passed = len(all_points) - grades[0]
pass_percentage = (passed / len(all_points)) * 100
print(f"Pass percentage: {pass_percentage:.1f}")

# grade distribution
print("Grade distribution:")
for i in range(5, -1, -1):
  stars = "*" * grades[i]
  print(f"  {i}: {stars}")