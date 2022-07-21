class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def even_odd_merge(L):

    if L is None:
        return L

    dummy_even = ListNode(0, None)
    dummy_odd = ListNode(0, None)
    chains = [dummy_even, dummy_odd]

    idx = 0
    while L:

        chains[idx].next = L
        L = L.next
        chains[idx] = chains[idx].next
        idx ^= 1

    chains[0].next = dummy_odd.next
    chains[1].next = None

    return dummy_even.next
