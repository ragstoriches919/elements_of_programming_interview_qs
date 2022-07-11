# Nailed it!!  Pretty easy...
def sinusoidal_string(s):

    top = ""
    mid = ""
    bottom = ""

    for i in range(1, len(s), 4):
        top += s[i]

    for i in range(0, len(s), 2):
        mid += s[i]

    for i in range(3, len(s), 4):
        bottom += s[i]

    return top + mid + bottom

print(sinusoidal_string("Hello World!"))