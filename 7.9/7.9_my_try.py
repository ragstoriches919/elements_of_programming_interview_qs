# This might work, but doesn't check for too many edge cases

class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def list_cyclic_right_shift(L, k):

    old_head = L
    curr = L
    prev = L

    for i in range(k-1):
        if i == 0:
            curr = curr.next
        else:
            curr = curr.next
            prev = prev.next

    prev.next = None

    while curr:
        curr = curr.next
        prev = prev.next

    prev.next = old_head

    return L

