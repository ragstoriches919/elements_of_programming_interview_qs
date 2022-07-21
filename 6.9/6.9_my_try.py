# no clue how to do this..
# my try from scratch after looking at the answer.

def get_valid_ip_address(s):

    def is_valid(s):
        return len(s) == 1 or (int(s) <= 255 and s[0] != "0")

    results = []
    parts = [''] * 4

    for i in range(1, min(4, len(s))):
        if is_valid(s[:i]):
            parts[0] = s[:i]

            for j in range(1, min(4, len(s) - i)):
                if is_valid(s[i:i+j]):
                    parts[1] = s[i:i+j]

                    for k in range(1, min(4, len(s)-i-j )):
                        if is_valid(s[i+j: i+j+k]) and is_valid(s[i+j+k:]):
                            parts[2] = s[i+j: i+j+k]
                            parts[3] = s[i+j+k:]
                            results.append('.'.join(parts))

    return results


ip = "19216811"
print(get_valid_ip_address(ip))

