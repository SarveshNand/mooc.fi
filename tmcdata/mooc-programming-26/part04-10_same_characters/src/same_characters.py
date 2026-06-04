# Write your solution here
def same_chars(a, b, c):
    if b >= len(a) or c >= len(a):
        return False
    return a[b] == a[c]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))