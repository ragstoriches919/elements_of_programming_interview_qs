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


# Linked List 1
L1 = LinkedList()

n2 = Node(7)
n5 = Node(5)
n7 = Node(2)

L1.add_node(n2)
L1.add_node(n5)
L1.add_node(n7)

# Linked list 2
L2 = LinkedList()

n3 = Node(11)
n11 = Node(3)

L2.add_node(n3)
L2.add_node(n11)

print("hi")

while L1.head != None and L2.head != None:


