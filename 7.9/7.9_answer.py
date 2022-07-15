class ListNode:

    def __init__(self, data = 0, next = next):
        self.data = data
        self.next = next


def cycle_right(L, k):

    if L is None or k == 0:
        return L

    length = 0
    tail = L
    while L.next:
        tail = tail.next
        length += 1

    tail.next = L
    steps_to_new_head = length % k
    new_tail = tail

    for _ in steps_to_new_head:
        tail = tail.next
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head








