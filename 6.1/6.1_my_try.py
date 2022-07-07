val = "12355"


def string_to_int(val):
    if val[0] == "-":
        multiplier = -1
        val = val[1:]
    elif val[0] == "+":
        multiplier = 1
        val = val[1:]
    else:
        multiplier = 1

    sum = 0
    for i in range(len(val)):
        sum += (ord(val[~i]) - ord("0")) * 10 ** i

    return sum * multiplier


def int_to_string(val):

    sign = "-" if val <0 else "+"
    return_arr = []
    while True:
        return_arr.append( chr(ord("0") + val % 10))
        val //= 10
        if val == 0:
            break

    fin_string =  sign + "".join(reversed(return_arr))
    return fin_string


print(int_to_string(3445))