# Copy here code of line function from previous exercise and use it in your solution
def line(n, y):
    if y == "":
        print(n*"*")
    else:
        print(n*y[0])

def shape(a, b, c, d):
    for i in range(1, a + 1):
        line(i, b)

    for i in range(c):
        line(a, d)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")