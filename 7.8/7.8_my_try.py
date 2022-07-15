# Pretty good, I believe this works!

class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def remove_duplicates_sorted_list(L):

    dummy = ListNode(0, L)
    curr = dummy
    temp = L

    while curr and temp:
        while curr == temp:
            temp = temp.next
            if temp != curr:
                curr.next = temp

        temp = temp.next
        curr = curr.next

    return L
