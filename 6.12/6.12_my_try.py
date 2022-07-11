def search_for_substring(sub, s):

    if len(sub) > len(s):
        return -1

    for i in range(0, len(s)-len(sub) + 1):
        if s[i: i+len(sub)] == sub:
            return i

    return -1


print(search_for_substring("hat", "hat"))