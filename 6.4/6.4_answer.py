def replace_and_remove(size, s):

    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[i] = s[write_idx]
            write_idx +=1
        if s[i] == 'a':
            a_count +=1

    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx] = 'd'
            s[write_idx - 1] = 'd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1


    # cur_idx = write_idx - 1
    # write_idx += a_count - 1
    # final_size = write_idx + 1
    #
    # while cur_idx >= 0:
    #     if s[cur_idx] == 'a':
    #         s[write_idx - 1: write_idx + 1] = 'dd'
    #         write_idx -= 2
    #     else:
    #         s[write_idx] = s[cur_idx]
    #         write_idx
    #     cur_idx -= 1
    # print(s)
    # return final_size

replace_and_remove(6, [char for char in "abbcaa"])

