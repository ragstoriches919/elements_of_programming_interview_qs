# After seeing answer already

class ListNode:
    def __init__(self, data=0, next=Null):
        self.data = data
        self.next = next


class Solution:
    def reverse_sublist(self, L, start, finish):
        dummy = ListNode(data=0, next=L)
        curr = L
        prevLeft = dummy

        # Phase 1: iterate until you get to the start of the sublist reversal
        for _ in range(1, start):
            curr = curr.next
            prevLeft = curr

        # Phase 2: Do the sublist reversal
        prev = None
        for i in range(finish-start + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        # Phase 3:  Connect the sublist with the original list
        prevLeft.next.next = curr
        prevLeft.next = prev


