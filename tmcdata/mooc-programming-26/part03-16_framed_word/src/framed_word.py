# Write your solution here
word = input("Word: ")

frame_width = 30
inside_width = frame_width - 2

left_spaces = (inside_width - len(word)) // 2
right_spaces = inside_width - len(word) - left_spaces

print("*" * frame_width)
print("*" + " " * left_spaces + word + " " * right_spaces + "*")
print("*" * frame_width)