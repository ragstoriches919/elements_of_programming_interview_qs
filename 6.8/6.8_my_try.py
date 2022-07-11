# Roman numerals
# This works, but took me way too long i think.

def convert_roman(roman):

    i = 0
    sum = 0
    mappings = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000 }

    while i <= len(roman) - 1:
        if roman[i] in ["I", "X", "C"]:
            if i < len(roman) - 1 and roman[i: i+2] in ["IV", "IX", "XL", "XC", "CD","CM"]:
                sum += mappings[roman[i+1]] - mappings[roman[i]]
                i += 2
            else:
                sum += mappings[roman[i]]
                i+=1
        else:
            sum += mappings[roman[i]]
            i+=1

    return sum

print(convert_roman("MMXXII"))