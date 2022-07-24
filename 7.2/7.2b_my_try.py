# Reverse a linked list
# Got it, with some finagling, and checking youtube...but almost there

class ListNode:
    def __init__(self, data=0, next = None):
        self.data = data
        self.next = next


# class Solution():
def reverse_linked_list(first_node):
    dummy = ListNode(0, first_node)
    prev = dummy
    curr = first_node

    while curr:
        tempCurr = curr.next
        tempPrev = curr
        curr.next = prev
        curr = tempCurr
        prev = tempPrev

    return prev.next.data


node4 = ListNode(data=4, next=None)
node3 = ListNode(data=3, next=node4)
node2 = ListNode(data=2, next=node3)
node1 = ListNode(data=1, next=node2)



print(reverse_linked_list(node1))