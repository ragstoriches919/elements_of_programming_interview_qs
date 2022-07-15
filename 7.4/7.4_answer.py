def check_list_overlap(L0, L1):

    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    len_L0 = get_length(L0)
    len_L1 = get_length(L1)

    if len_L0 > len_L1:
        L0, L1 = L1, L0

    for _ in range(abs(len_L0-len_L1)):
        L1 = L1.next

    return L0 is L1
