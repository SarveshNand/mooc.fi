# Write your solution here
layers = int(input("Layers: "))

size = 2 * layers - 1

for i in range(size):
    row = ""
    for j in range(size):
        # distance to closest edge
        dist = min(i, j, size - 1 - i, size - 1 - j)

        # convert distance to letter
        letter = chr(ord('A') + layers - 1 - dist)

        row += letter

    print(row)