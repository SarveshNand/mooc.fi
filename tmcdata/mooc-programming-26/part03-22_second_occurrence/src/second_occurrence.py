
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

first = string.find(sub)

if first == -1:
    print("The substring does not occur twice in the string.")
else:
    second = string.find(sub, first + len(sub))

    if second == -1:
        print("The substring does not occur twice in the string.")
    else:
        print("The second occurrence of the substring is at index", second, end=".")