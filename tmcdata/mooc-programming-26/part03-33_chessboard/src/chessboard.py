# Write your solution here
def chessboard(size):
    for row in range(size):
        for column in range(size):
            if (row + column) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()
# Testing the function
if __name__ == "__main__":
    chessboard(3)