# Pretty sure this works!!

class ListNode:
    def __init__(self,data = 0, next = None):
        self.data = data
        self.next = next


def add_two_numbers(L1, L2):

    val1 = val2 = exponent = 0

    curr = L1

    while curr:
        val1 += curr.data * (10 ** exponent)
        exponent += 1

    curr = L2
    exponent = 0

    while curr:
        val2 += curr.data * (10 ** exponent)
        exponent += 1

    sum = val1 + val2
    dummy = ListNode(0, None)
    curr = dummy

    while sum:
        curr.next = ListNode(sum % 10, None)
        sum //= 10

    return dummy.next



