# Absolutely nailed it...and very quickly too!!

def test_palindrome(word):

    dict_counts = {}

    for ch in word:
        if ch in dict_counts:
            dict_counts[ch] += 1
        else:
            dict_counts[ch] = 1

    num_even = 0
    num_odd = 0

    for val in dict_counts.values():
        if val % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    return num_odd <= 1


print(test_palindrome("edified"))