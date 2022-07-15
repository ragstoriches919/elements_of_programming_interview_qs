# My try after looking at answer

class ListNode:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next


def overlapping_no_cycle_lists(L0, L1):

    def length(head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    L0_len = length(L0)
    L1_len = length(L1)

    if L0_len > L1_len:
        L1, L0 = L0, L1

    for _ in range(abs(length(L0) - length(L1))):
        L1 = L1.next

    while L0 and L1 and L0 is not L1:
        L0 = L0.next
        L1 = L1.next

    return L0
