class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def even_odd_merge(L):

    even = L
    if even.next:
        odd = even.next
    else:
        return L

    while even:

        if even.next is None or even.next.next is None:
            even.next = odd

        else:
            even = even.next.next

    while odd:
        if odd.next is None or odd.next.next is None:
            odd.next = None
        else:

            odd = odd.next.next

    return L

