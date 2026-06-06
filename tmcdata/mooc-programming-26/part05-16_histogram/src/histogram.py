# Write your solution here
def histogram(word: str):
    counts = {}

    # Count occurrences
    for letter in word:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1

    # Print histogram (in order of first appearance)
    for letter in counts:
        print(f"{letter} " + "*" * counts[letter])