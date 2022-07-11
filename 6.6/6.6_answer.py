def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start += 1
            finish -= 1

    reverse_range(s, 0, len(s) - 1)
    start = 0
    print(s)
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        if finish == len(s):
            break
        reverse_range(s, start, finish - 1)
        start = finish + 1

    reverse_range(s, start, len(s) - 1)
    print(s)
    return s

sentence = [char for char in "ram is costly"]
reverse_words(sentence)