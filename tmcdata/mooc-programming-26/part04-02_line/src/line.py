# Write your solution here
def line(n, y):
    if y == "":
        print(n*"*")
    else:
        print(n*y[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")