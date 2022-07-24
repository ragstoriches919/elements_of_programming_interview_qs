def well_formed_string(s):

    dict_chars = {"{": "}", "(": ")", "[": "]"}
    stack = []

    for ch in s:
        if ch in dict_chars:
            stack.append(ch)
        else:
            if ch != dict_chars[stack.pop()]:
                return False

    return len(stack) == 0

s = "([]){()}"

print(well_formed_string(s))