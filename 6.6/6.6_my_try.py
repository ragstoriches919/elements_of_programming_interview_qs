# This absolutely works!

def reverse_sentence(sentence):
    sentence = sentence.split(" ")

    for i in range(len(sentence)//2):
        sentence[i], sentence[~i] = sentence[~i], sentence[i]

    return " ".join(sentence)

s = "Ten animals I slam in a net"
# s = "Alice likes Bob"
print(reverse_sentence(s))
