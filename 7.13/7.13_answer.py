# Not bad, this makes sense to me!!

class ListNode:
    def __init__(self,data = 0, next = None):
        self.data = data
        self.next = next


def add_two_numbers(L1, L2):

    dummy_head = curr = ListNode(0, None)
    val = 0
    carry = 0

    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        curr.next = ListNode(val % 10 , None)
        curr = curr.next
        carry = val // 10

    return dummy_head.next

