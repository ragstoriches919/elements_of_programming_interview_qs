# got it right... a bit tricky on the encoding part, but not bad.

def decoding(s):

    num = ""
    return_code = ""
    for i in range(0, len(s)):
        if s[i].isnumeric():
            num += s[i]
        else:
            return_code += s[i] * int(num)
            num = ""

    return return_code


def encoding(s):
    count = 1
    code = ""

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            code += str(count) + s[i-1]
            count = 1

    code += str(count) + s[i - 1]

    return code


s ="eeeffffee"
print(encoding(s))
