class ListNode():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None


class Solution():
    def merge_two_lists(self, L1, L2):
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

        tail.next = L1 or L2
        return dummy.next

