# Write your solution here
def first_word(s):
    first = s.split(" ")
    fw = first[0]
    return fw
def second_word(s):
    second = s.split(" ")
    sw = second[1]
    return sw
def last_word(s):
    last = s.split(" ")
    lw = last[-1]
    return lw
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))