# Had to look at answers a bunch

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution():
    def mergeTwoLists(self, L1: ListNode, L2:ListNode):
        dummy = ListNode()
        tail = dummy

        while L1 and L2:
            if L1.data <= L2.data:
                tail.next = L1
                L1 = L1.next

            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next

        # Append whatever is remaining
        tail.next = L1 or L2

        return dummy.next



