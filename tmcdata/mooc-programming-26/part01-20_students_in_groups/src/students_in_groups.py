# Write your solution here
std = int(input("How many students on the course? "))
group = int(input("Desired group size? "))

groups = std // group
if std % group != 0:
  groups += 1

print("Number of groups formed:", groups)