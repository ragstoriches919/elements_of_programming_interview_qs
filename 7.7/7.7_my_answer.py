# I've already seen the solution, trying to recreate it
class ListNode:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next


def remove_kth_element(L, k):

    dummy = ListNode(0, L)
    first = L
    second = dummy

    for _ in range(k):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next


def remove_kth_element_redo(L, k):

    dummy = ListNode(0, L)
    first = L
    second = dummy

    for _ in range(k):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return L

