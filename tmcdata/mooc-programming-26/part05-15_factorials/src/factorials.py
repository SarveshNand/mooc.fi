# Write your solution here
def factorials(n: int):
    result = {}
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        result[i] = fact

    return result