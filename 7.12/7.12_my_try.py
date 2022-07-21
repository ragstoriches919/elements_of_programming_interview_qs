# Pretty much got the gist of it.
# I think my solution with the list also works!

class ListNode:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next


def get_ll_pivot_list(head, pivot):

    lesser_dummy = ListNode()
    equal_dummy = ListNode()
    greater_dummy = ListNode()

    lesser=lesser_dummy
    equal = equal_dummy
    greater = greater_dummy

    curr = head

    while curr:
        if curr.data < pivot:
            lesser.next = curr
            lesser = lesser.next
        elif curr.data == pivot:
            equal.next = curr
            equal = equal.next
        else:
            greater.next = curr
            greater = greater.next

        curr = curr.next

    lesser.next = equal_dummy.next
    equal.next = greater_dummy.next
    greater.next = None

    return lesser_dummy.next

