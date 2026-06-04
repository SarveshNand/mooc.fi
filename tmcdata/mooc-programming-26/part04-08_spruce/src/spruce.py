# Write your solution here
def spruce(x):
    print("a spruce!")
    for i in range(x):
        spaces = x - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

    print(" " * (x - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)