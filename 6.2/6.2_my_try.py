# Got it right!!

def base_change(b1, b2,num_as_string):

    val = 0
    for i in range(0, len(num_as_string)):
        val += int(num_as_string[~i]) * (b1 **i)

    dict_map = {"10": "A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F", "16":"G" }

    # power = 1
    ret_str = ""
    while val !=0:
        digit = val % b2
        val -= digit
        val //=b2

        digit_str = str(digit) if digit <10 else dict_map[str(digit)]
        ret_str += digit_str

    return ret_str

print(base_change(10, 16, "15332"))
