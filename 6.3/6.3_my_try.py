# ABSOLUTELY DEMOLISHED THIS Q. Nice!!

def excel_col_to_num(col_str):
    col_num = 0
    for i in range(len(col_str)):
        mult = ord(col_str[~i]) - ord("A") + 1
        col_num += mult * (26 ** i)
    print(col_num)

excel_col_to_num("ZZ")