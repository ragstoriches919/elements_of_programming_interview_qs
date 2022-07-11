# replicating the actual answer.
# It doesn't seem to work...but i learned about curr index, write index, etc.

def replace_and_remove(size, s):
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx +=1
        if s[i] == 'a':
            a_count +=1

    print(s)

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    while cur_idx > 0:
        if s[cur_idx] == 'a':
            s[write_idx] = 'd'
            s[write_idx -1] = 'd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    print(s)
    return final_size



replace_and_remove(5, [char for char in "abcaa     "])














# not a legit method...
def chg(arr, size):
    arr = "".join(arr)
    arr = arr.replace("a", "dd")
    arr = arr.replace("b", "")
    arr = [char for char in arr]
    return arr

test = ["a", "c", "d", "b", "b","c", "a"]

# print(chg(test, 5))
