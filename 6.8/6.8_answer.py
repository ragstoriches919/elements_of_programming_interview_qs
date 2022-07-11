# Found this answer here:  https://www.tutorialspoint.com/roman-to-integer-in-python
# Book answer is annoying

def roman_to_integer(roman):
    mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                "CD": 400, "CM": 900}

    i = 0
    sum = 0

    while i < len(roman):
        if i < len(roman) - 1 and roman[i:i+2] in mappings:
            sum += mappings[roman[i:i+2]]
            i += 2
        else:
            sum += mappings[roman[i]]
            i += 1

    return sum

print(roman_to_integer("M"))