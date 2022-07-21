import collections


def ransom_letter(letter, magazine):

    dict_letter = {}
    dict_magazine = {}

    for ch in letter:
        if ch not in dict_letter:
            dict_letter[ch] = 1
        else:
            dict_letter[ch] += 1

    for ch in magazine:
        if ch not in dict_magazine:
            dict_magazine[ch] = 1
        else:
            dict_magazine[ch] += 1

    for key, val in dict_letter.items():
        if key not in dict_magazine or val > dict_magazine[key]:
            return False

    return True


def test(letter, magazine):
    y = collections.Counter(letter)
    print(y)

letter = "ten animal i slam in a net"
magazine = "catss"

test(letter, magazine)

#
# print(ransom_letter(letter, magazine))
